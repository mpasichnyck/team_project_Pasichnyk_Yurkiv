# Частина Максима
import yfinance as yf
import pandas as pd
import maksym_code
import sonya_code
import csv
import json
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
strategy, total_pnl = sonya_code.strategy(profits)
with open("extra files to project/our_profits_data", "w", newline="") as file:
    writer = csv.DictWriter(file,fieldnames=["Buy_Date","Buy_Price","Sell_Date","Sell_Price","P&L"])
    writer.writeheader()
    writer.writerows(profits)
# Частина Максима
maksym_code.graph_result(df)
print(f"Our total P&L is {round(total_pnl,2)}")
print("------------------------------")
print(f"List of our profits for this active: \n {profits}")
print("------------------------------")
print(f"Our efficiency of strategy: \n total_trades:{strategy["total_trades"]} \n profitable_trades:{strategy["profitable_trades"]} \n losing_trades:{strategy["losing_trades"]} \n total_pnl:{strategy["total_pnl"]} \n win_rate:{strategy["win_rate"]}% ")


