import yfinance as yf
import pandas as pd
import maksym_code
import sonya_code
import csv
data = yf.download(
    "AAPL",
    start="2020-01-01",
    end="2026-07-01"
)
df=pd.DataFrame(data)
df.columns = df.columns.get_level_values(0)
df=maksym_code.clean_data(df)
df=maksym_code.calculate_moving_average(df)
df=maksym_code.signals(df)
with open("extra files to project/applebuysell.csv", "w") as file:
    df.to_csv(file)
# частина Соні
df, profits = sonya_code.calculate_pnl(df)
print(profits)
strategy = sonya_code.strategy(profits)
print(strategy)


