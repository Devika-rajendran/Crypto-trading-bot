from bot import BasicBot
from strategies import twap_strategy

# Simulation mode — no real API keys needed
bot = BasicBot()

symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
side = input("Enter side (BUY/SELL): ").upper()
order_type = input("Order type (MARKET / LIMIT / TWAP): ").upper()

if order_type == "MARKET":
    qty = float(input("Quantity: "))
    bot.place_market_order(symbol, side, qty)

elif order_type == "LIMIT":
    qty = float(input("Quantity: "))
    price = float(input("Price: "))
    bot.place_limit_order(symbol, side, qty, price)

elif order_type == "TWAP":
    total_qty = float(input("Total quantity: "))
    slices = int(input("Number of slices: "))
    delay = int(input("Delay between orders (seconds): "))
    twap_strategy(bot, symbol, side, total_qty, slices, delay)

else:
    print("Invalid order type")
