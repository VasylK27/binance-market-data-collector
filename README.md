# Binance Market Data Collector (CLI Version)

A simple, modular Python tool designed to fetch, process, and store historical market data (Klines/Candlesticks) from the Binance Spot API.

---

## 💼 Professional Context

This project demonstrates:
- GUI application development (PySide6)
- Multithreading and async workflows
- Browser automation with stealth techniques
- Data extraction and normalization
- Export pipelines for analytics

---

## 🚀 Features
- **Interactive CLI**: Users can specify Symbol (e.g., BTCUSDT), Interval (e.g., 1h, 1d), and Limit via command line.
- **Robust Error Handling**: Uses `try-except` blocks and status checks to handle network issues and invalid user inputs.
- **Professional Logging**: Implements the `logging` module with timestamps to track application flow and errors.
- **Data Transformation**: Converts raw API responses into cleaned, typed Pandas DataFrames (float64 for prices).
- **CSV Export**: Automatically saves processed data to local CSV files for further analysis.
- **Modular Design**: Clean separation between API logic, data utilities, and the main execution flow.

---

## 🛠 Tech Stack
- **Python 3.10+**
- **Pandas**: For high-performance data manipulation.
- **Requests**: For reliable HTTP communication with Binance API.
- **Logging**: For system monitoring and debugging.

---

## 📁 Project Structure
- `main.py`: The entry point. Handles user interaction and application flow.
- `scraper.py`: Logic for communicating with the Binance API.
- `utils.py`: Data formatting, DataFrame cleaning, and file I/O.
- `requirements.txt`: List of necessary Python packages.

## ⚙️ Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VasylK27/binance-market-data-collector
   cd binance-market-data-collector
