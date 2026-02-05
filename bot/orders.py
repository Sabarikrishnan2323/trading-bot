import logging

def place_order(client, order_data):
    try:
    
        if order_data["type"] == "LIMIT":
            order_data["timeInForce"] = "GTC"

        logging.info(f"API Request: {order_data}")

        order = client.futures_create_order(**order_data)

        logging.info(f"API Response: {order}")

        if not order:
            raise Exception("Empty response from Binance")

        return order

    except Exception as e:
        logging.error(f"Order failed: {e}")
        raise Exception(f"Order rejected by Binance: {e}")
