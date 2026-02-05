# Binance Futures Testnet Trading Bot (Python)

## Prerequisites

- Python **3.10 or higher**
- Binance **Futures Testnet** account
- `python-binance` library

---

## Setup Steps

1. Clone the repository:
```

git clone https://github.com/Sabarikrishnan2323/trading-bot.git
cd trading-bot

```


2. Install dependencies:
```

pip install python-binance

```

3. Set Binance Futures Testnet API credentials as environment variables.

**Windows PowerShell:**
```

$Env:BINANCE_API_KEY="YOUR_TESTNET_API_KEY"
$Env:BINANCE_API_SECRET="YOUR_TESTNET_API_SECRET"

```

4. Restart the terminal if required.

---

## How to Run

Run the CLI:
```

python cli.py

```

---

## MARKET Order Example
```

Enter symbol (e.g. BTCUSDT): BTCUSDT
Enter side (BUY / SELL): BUY
Order type (MARKET / LIMIT / STOP): MARKET
Quantity: 0.001

```

---

## LIMIT Order Example
```

Enter symbol (e.g. BTCUSDT): BTCUSDT
Enter side (BUY / SELL): BUY
Order type (MARKET / LIMIT / STOP): LIMIT
Quantity: 1
Limit price: 66732

```

---
