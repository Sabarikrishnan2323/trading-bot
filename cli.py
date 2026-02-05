import os
import time
import logging
from binance.client import Client
from bot.orders import place_order
from bot.logging_config import setup_logging

setup_logging()

def main():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise EnvironmentError("Missing API keys")

    client = Client(api_key, api_secret, testnet=True)

    
    server_time = client.get_server_time()["serverTime"]
    local_time = int(time.time() * 1000)
    client.timestamp_offset = server_time - local_time
    client.RECV_WINDOW = 10000

    logging.info("Binance Futures Testnet client initialized")

    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Enter side (BUY / SELL): ").upper()
    order_type = input("Order type (MARKET / LIMIT / STOP): ").upper()
    quantity = float(input("Quantity: "))

    order_data = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    
    if order_type == "LIMIT":
        price = float(input("Limit price: "))
        order_data["price"] = price

    print("\nOrder Request Summary")
    for k, v in order_data.items():
        print(f"{k}: {v}")

    order = place_order(client, order_data)

    print("\n✅ Order Sent")
    print(f"Order ID     : {order.get('orderId')}")
    print(f"Status       : {order.get('status')}")
    print(f"Executed Qty : {order.get('executedQty')}")
    print(f"Avg Price    : {order.get('avgPrice', 'N/A')}")

if __name__ == "__main__":
    main()
