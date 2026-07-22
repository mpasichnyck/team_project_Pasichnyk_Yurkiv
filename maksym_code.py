import yfinance as yf
import pandas as pd
data = yf.download(
    "AAPL",
    start="2020-01-01",
    end="2026-07-01"
)
df=pd.DataFrame(data)
def clean_data(df):
    df=df.dropna()
    df = df.drop_duplicates()
    df = df.sort_index()
    return df
def calculate_moving_average(df):
    df["Short_MA"]=df["Close"].rolling(window=20).mean()
    df["Long_MA"]=df["Close"].rolling(window=50).mean()
