import requests
import pandas as pd

SPOT_KLINES_URL = "https://api.binance.com/api/v3/klines"

def get_spot_klines(symbol: str, interval: str, limit: int):
    """
    The function is for getting spot klines from Binance.
    
    :param symbol: for example - BTCUSDT
    :type symbol: str
    :param interval: for example - 1h
    :type interval: str
    :param limit: for example - 10
    :type limit: int
    :return: list or None
    """
    params = {
            'symbol': symbol,
            'interval': interval,
            'limit': limit
        }
    
    try:
        data = requests.get(SPOT_KLINES_URL, params=params)
        data.raise_for_status()
        return data.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
