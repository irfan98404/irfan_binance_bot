import sys
from datetime import datetime
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logger import setup_logger



# ---------------- LOGGING SETUP ----------------
logger = setup_logger()

# ---------------- VALIDATION ----------------
def validate_inputs(symbol, side, quantity, take_profit, stop_loss):
    if not symbol.endswith("USDT"):
        raise ValueError("Invalid symbol. Must end with USDT")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    quantity = float(quantity)
    take_profit = float(take_profit)
    stop_loss = float(stop_loss)

    if quantity <= 0 or take_profit <= 0 or stop_loss <= 0:
        raise ValueError("Quantity and prices must be positive")

    return symbol, side, quantity, take_profit, stop_loss


# ---------------- MOCK OCO ORDER ----------------
def place_oco_order(symbol, side, quantity, take_profit, stop_loss):
    oco_order = {
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "take_profit": take_profit,
        "stop_loss": stop_loss,
        "status": "OCO_PLACED",
        "time": datetime.utcnow().isoformat()
    }

    logger.info(f"OCO Order Placed: {oco_order}")

    print("✅ OCO Order Placed Successfully")
    print("Take Profit Order:", take_profit)
    print("Stop Loss Order:", stop_loss)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            "Usage: python src/advanced/oco.py SYMBOL BUY/SELL QUANTITY TAKE_PROFIT STOP_LOSS"
        )
        sys.exit(1)

    try:
        symbol, side, quantity, tp, sl = validate_inputs(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4],
            sys.argv[5]
        )
        place_oco_order(symbol, side, quantity, tp, sl)

    except Exception as e:
        logger.error(str(e))
        print("❌ Error:", e)
