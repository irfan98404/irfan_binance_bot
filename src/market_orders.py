import sys
from logger import setup_logger
from datetime import datetime

# ---------------- LOGGING SETUP ----------------
logger = setup_logger()
logger.info(...)
logger.error(...)

# ---------------- VALIDATION ----------------
def validate_inputs(symbol, side, quantity):
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

    return symbol, side, quantity


# ---------------- MOCK MARKET ORDER ----------------
def place_market_order(symbol, side, quantity):
    # This is a simulated order (NO API)
    order = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity,
        "status": "FILLED",
        "price": "MARKET_PRICE",
        "time": datetime.utcnow().isoformat()
    }

    logger.info(f"Market Order Executed: {order}")
    print("✅ Market Order Placed Successfully")
    print(order)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python src/market_orders.py SYMBOL BUY/SELL QUANTITY")
        sys.exit(1)

    try:
        symbol, side, quantity = validate_inputs(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
        place_market_order(symbol, side, quantity)

    except Exception as e:
        logger.error(str(e))
        print("❌ Error:", e)
