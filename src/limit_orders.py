import sys
from logger import setup_logger
from datetime import datetime

# ---------------- LOGGING SETUP ----------------

logger = setup_logger()



# ---------------- VALIDATION ----------------
def validate_inputs(symbol, side, quantity, price):
    if not symbol.endswith("USDT"):
        raise ValueError("Invalid symbol. Must end with USDT (e.g., BTCUSDT)")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
    except:
        raise ValueError("Quantity must be a positive number")

    try:
        price = float(price)
        if price <= 0:
            raise ValueError
    except:
        raise ValueError("Price must be a positive number")

    return symbol, side, quantity, price


# ---------------- MOCK LIMIT ORDER ----------------
def place_limit_order(symbol, side, quantity, price):
    order = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "status": "NEW",
        "time": datetime.utcnow().isoformat()
    }
    logger.info(f"Market Order Executed: {order}")

    logger.info(f"Limit Order Placed: {order}")
    print("✅ Limit Order Placed Successfully")
    print(order)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python src/limit_orders.py SYMBOL BUY/SELL QUANTITY PRICE")
        sys.exit(1)

    try:
        symbol, side, quantity, price = validate_inputs(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
        )
        place_limit_order(symbol, side, quantity, price)

    except Exception as e:
        logger.error(str(e))
        print("❌ Error:", e)
