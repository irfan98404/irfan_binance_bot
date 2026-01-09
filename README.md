# Binance Futures Order Bot (CLI-Based)

## 📌 Project Overview
This project is a **CLI-based trading bot** developed for **Binance USDT-M Futures**.  
It supports **core order types** and **advanced trading strategies**, with proper **input validation**, **structured logging**, and **modular design**.

The bot is designed to be extensible and can be easily connected to the real Binance Futures API or Testnet.

---

## ⚙️ Features Implemented

### ✅ Core Orders (Mandatory)
- Market Order
- Limit Order

### ⭐ Advanced Orders
- OCO (One-Cancels-the-Other)
- TWAP (Time-Weighted Average Price)

### 🛡 Validation & Logging
- Input validation for symbol, side, quantity, and price
- Centralized logging system (`bot.log`)
- Logs all actions and errors with timestamps

---
### OCO (One-Cancels-the-Other)

Binance USDT-M Futures does not support native OCO orders like Spot trading.
Additionally, during development and testing on Binance Futures Testnet,
position-level Take-Profit and Stop-Loss orders (`STOP_MARKET`,
`TAKE_PROFIT_MARKET`) may return API constraint errors when re-placed
programmatically.

To address this, OCO is implemented as a **logical strategy** at the
application layer. The bot links a Take-Profit and a Stop-Loss order
conceptually and manages them through structured logging and execution
control.

This approach reflects how professional futures trading systems handle
risk management while remaining compliant with Binance Futures constraints.

