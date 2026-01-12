# ui.py
import streamlit as st
from bot import BasicBot
from strategies import twap_strategy

# --- Initialize simulation bot ---
if "bot" not in st.session_state:
    st.session_state.bot = BasicBot(starting_balance=10000)

bot = st.session_state.bot

st.title("📈 Simulated Trading Bot")

# --- Show current portfolio ---
st.subheader("Portfolio")
st.write(f"💰 Balance: ${bot.balance:.2f}")
if bot.positions:
    st.write("📊 Positions:")
    for symbol, qty in bot.positions.items():
        st.write(f"- {symbol}: {qty}")
else:
    st.write("No positions yet.")

st.markdown("---")

# --- Order inputs ---
st.subheader("Place an Order")

symbol = st.text_input("Symbol (e.g., BTCUSDT)").upper()
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "TWAP"])

# --- MARKET / LIMIT inputs ---
qty = st.number_input("Quantity", min_value=0.000001, value=0.001, format="%.6f")
price = None
if order_type in ["LIMIT", "TWAP"]:
    price = st.number_input("Price (Optional for TWAP)", min_value=0.000001, value=1.0, format="%.6f")

# --- TWAP inputs ---
total_qty = slices = delay = None
if order_type == "TWAP":
    total_qty = st.number_input("Total quantity", min_value=0.000001, value=0.01, format="%.6f")
    slices = st.number_input("Number of slices", min_value=1, value=5)
    delay = st.number_input("Delay between slices (seconds)", min_value=0, value=1)

# --- Place order button ---
if st.button("Place Order"):
    result = None

    if order_type == "MARKET":
        result = bot.place_market_order(symbol, side, qty)
    elif order_type == "LIMIT":
        result = bot.place_limit_order(symbol, side, qty, price)
    elif order_type == "TWAP":
        # TWAP strategy can place multiple orders, handle individually inside strategy
        result = twap_strategy(bot, symbol, side, total_qty, slices, delay, price)
    else:
        st.error("Invalid order type")

    # --- Handle result ---
    if isinstance(result, dict) and "error" in result:
        st.error(f"❌ {result['error']}")
    elif isinstance(result, list):
        # In case TWAP returns multiple orders
        st.success("✅ TWAP orders executed!")
        for r in result:
            st.write(f"{r['side']} {r['qty']} {r['symbol']} at {r['price']} ({r['type']})")
    else:
        st.success(f"✅ Order executed: {result['side']} {result['qty']} {result['symbol']} at {result['price']} ({result['type']})")

# --- Show all past orders ---
st.subheader("Order History")
if bot.orders:
    st.table(bot.orders)
else:
    st.write("No orders placed yet.")
