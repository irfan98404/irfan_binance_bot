import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logger import setup_logger
from binance_client import get_client

# ---------------- LOGGING SETUP ----------------
logger = setup_logger()

# ---------------- VALIDATION ----------------
def validate_inputs(symbol, side, quantity, take_profit, stop_loss):
    if not symbol.endswith("USDT"):
        raise ValueError("Invalid symbol")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    quantity = float(quantity)
    take_profit = float(take_profit)
    stop_loss = float(stop_loss)

    if quantity <= 0 or take_profit <= 0 or stop_loss <= 0:
        raise ValueError("Quantity and prices must be positive")

    return symbol, side, quantity, take_profit, stop_loss


# ---------------- REAL OCO (FUTURES LOGICAL) ----------------
def place_oco_order(symbol, side, quantity, take_profit, stop_loss):
    client = get_client()

    opposite_side = "SELL" if side == "BUY" else "BUY"

    # Take Profit Order
    tp_order = client.futures_create_order(
        symbol=symbol,
        side=opposite_side,
        type="TAKE_PROFIT_MARKET",
        stopPrice=take_profit,
        closePosition=True
    )

    # Stop Loss Order
    sl_order = client.futures_create_order(
        symbol=symbol,
        side=opposite_side,
        type="STOP_MARKET",
        stopPrice=stop_loss,
        closePosition=True
    )

    logger.info(f"OCO Orders Placed | TP: {tp_order} | SL: {sl_order}")

    print("✅ OCO Orders Placed Successfully")
    print("✅ OCO Orders Placed Successfully")

    print("Take Profit Order Response:")
    print(tp_order)

    print("Stop Loss Order Response:")
    print(sl_order)



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
