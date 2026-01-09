import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import time
from logger import setup_logger
from binance_client import get_client

# ---------------- LOGGING SETUP ----------------
logger = setup_logger()

# ---------------- VALIDATION ----------------
def validate_inputs(symbol, side, total_qty, slices, interval):
    if not symbol.endswith("USDT"):
        raise ValueError("Invalid symbol")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    total_qty = float(total_qty)
    slices = int(slices)
    interval = int(interval)

    if total_qty <= 0 or slices <= 0 or interval <= 0:
        raise ValueError("Invalid inputs")

    return symbol, side, total_qty, slices, interval


# ---------------- REAL TWAP ----------------
def place_twap_order(symbol, side, total_qty, slices, interval):
    client = get_client()
    qty_per_order = round(total_qty / slices, 6)

    print("📊 TWAP Execution Started")
    logger.info(
        f"TWAP Started | Symbol={symbol}, Side={side}, TotalQty={total_qty}, Slices={slices}"
    )

    for i in range(1, slices + 1):
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty_per_order
        )

        logger.info(f"TWAP Slice {i} Executed: {order}")
        print(f"✅ Slice {i}/{slices} executed → Qty: {qty_per_order}")

        if i < slices:
            time.sleep(interval)

    print("🎉 TWAP Execution Completed")
    logger.info("TWAP Execution Completed")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            "Usage: python src/advanced/twap.py SYMBOL BUY/SELL TOTAL_QTY SLICES INTERVAL"
        )
        sys.exit(1)

    try:
        symbol, side, qty, slices, interval = validate_inputs(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4],
            sys.argv[5]
        )

        place_twap_order(symbol, side, qty, slices, interval)

    except Exception as e:
        logger.error(str(e))
        print("❌ Error:", e)
