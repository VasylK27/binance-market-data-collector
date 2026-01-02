import pandas as pd

def format_klines(raw_data: list):
    """
    Function for formating data in usable data frame
    
    :param raw_data: list of data from cryptocurrency
    :type raw_data: list
    :return pandas dataframe
    """

    if not raw_data:
        return pd.DataFrame()

    columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
            'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
            'taker_buy_quote_asset_volume', 'ignore']
    
    df = pd.DataFrame(raw_data, columns=columns)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df = df[['open', 'high', 'low', 'close', 'volume']].astype(float)

    return df


def save_to_csv(df: pd.DataFrame, filename: str):
    """
    Saves the DataFrame to a CSV file.
    
    :param df: data from format_klines.
    :type df: pd.DataFrame
    :param filename: for diferent requests different names of file.
    :type filename: str
    """

    try:
        df.to_csv(filename)
        print(f"Successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")
