class BasicBot:
    def __init__(self, starting_balance=10000):
        """
        Simulation mode bot.
        starting_balance: virtual USD balance
        """
        self.balance = starting_balance  # USD
        self.positions = {}  # symbol -> quantity
        self.orders = []

    def place_market_order(self, symbol, side, qty, price=None):
        """
        Execute a market order instantly.
        """
        mock_price = price if price else 50000  # default mock price
        cost = qty * mock_price

        if side == "BUY":
            if self.balance < cost:
                return {"error": f"Insufficient balance to buy {qty} {symbol}"}
            self.balance -= cost
            self.positions[symbol] = self.positions.get(symbol, 0) + qty
        elif side == "SELL":
            if self.positions.get(symbol, 0) < qty:
                return {"error": f"Not enough {symbol} to sell {qty}"}
            self.positions[symbol] -= qty
            self.balance += cost
        else:
            return {"error": "Invalid side. Must be 'BUY' or 'SELL'"}

        order = {
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "qty": qty,
            "price": mock_price
        }
        self.orders.append(order)
        print(f"[SIMULATION] MARKET order executed: {order}")
        return order

    def place_limit_order(self, symbol, side, qty, price, execute_immediately=False):
        """
        Place a limit order.
        If execute_immediately=True, simulate instant execution.
        """
        order = {
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "qty": qty,
            "price": price
        }
        self.orders.append(order)
        print(f"[SIMULATION] LIMIT order placed at {price}: {order}")

        # Only execute immediately if explicitly True
        if execute_immediately:
            result = self.place_market_order(symbol, side, qty, price)
            if "error" in result:
                print(f"[SIMULATION] LIMIT execution failed: {result['error']}")
            else:
                print(f"[SIMULATION] LIMIT order executed: {result}")

        return order  # make sure return is outside the if

    def get_portfolio(self):
        """
        Return current balance and positions.
        """
        return {
            "balance": self.balance,
            "positions": self.positions.copy(),
            "orders": self.orders.copy()
        }
