# strategies.py
import time

def twap_strategy(bot, symbol, side, total_qty, slices, delay, price=None):
    """
    Simulate TWAP orders: split total_qty into slices
    Each slice will be recorded as type 'TWAP'
    """
    slice_qty = total_qty / slices
    orders = []

    for i in range(1, slices + 1):
        # Execute a simulated market order
        order = bot.place_market_order(symbol, side, slice_qty, price)
        
        # Override the order type to TWAP for order history
        order['type'] = 'TWAP'
        bot.orders[-1] = order  # update the last appended order
        
        orders.append(order)
        print(f"[SIMULATION] TWAP slice {i}/{slices} executed: {order}")
        time.sleep(delay)

    return orders
