from scraper import get_spot_klines
from utils import format_klines, save_to_csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("--- Binance Data Collector ---")

    symbol = input("Enter symbol (default BTCUSDT): ").upper().strip() or "BTCUSDT"
    interval = input("Enter interval (e.g., 1m, 5m, 1h, 1d): ").strip() or "1h"
    
    try:
        limit_input = input("Enter limit (default 100): ").strip()
        limit = int(limit_input) if limit_input else 100
    except ValueError:
        logging.error("Invalid limit. Using default 100.")
        limit = 100

    logging.info(f"\nFetching {limit} candles for {symbol} ({interval})...")
    raw_data = get_spot_klines(symbol, interval, limit)

    if raw_data:
        df = format_klines(raw_data)
        
        if not df.empty:
            filename = f"{symbol}_{interval}.csv"
            
            save_to_csv(df, filename)
            
            logging.info("\nPreview of the data:")
            print(df.head())
        else:
            logging.error("Transformation failed: DataFrame is empty.")
    else:
        logging.info("Failed to fetch data from Binance.")

if __name__ == "__main__":
    main()
