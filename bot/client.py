import logging
from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        logging.info("Binance Futures Testnet client initialized")

    def create_order(self, order_data: dict):
        logging.info(f"API Request: {order_data}")
        response = self.client.futures_create_order(
    **order_data,
    recvWindow=5000,
    newOrderRespType="RESULT"
)

        logging.info(f"API Response: {response}")
        return response
