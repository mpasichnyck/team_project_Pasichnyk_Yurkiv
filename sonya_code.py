import matplotlib.pyplot as plt
def calculate_pnl(df):
    profits = []
    buy_price = None
    buy_date = None
    for i in range(len(df)):
        signal = df.iloc[i]['Signal']
        price = df.iloc[i]['Close']
        date = df.index[i]
        if signal == 'BUY' and buy_price is None:
            buy_price = float(price)
            buy_date = date
        elif signal == 'SELL' and buy_price is not None:
            sell_price = float(price)
            sell_date = date
            profit = float(sell_price - buy_price)
            profits.append({"Buy_Date": buy_date,
                            "Buy_Price": buy_price,
                            "Sell_Date": sell_date,
                            "Sell_Price": sell_price,
                            "P&L": profit})
            buy_price = None
            buy_date = None
    return df,profits
def strategy(profits):
    amount_of_trades = len(profits)
    profitable_trades = 0
    losing_trades = 0
    for trade in profits:
        if trade['P&L'] > 0:
            profitable_trades += 1
        elif trade['P&L'] < 0:
            losing_trades += 1
    total_pnl = sum(profit["P&L"] for profit in profits)
    if amount_of_trades>0:
        win_rate = (profitable_trades/amount_of_trades)*100
    else:
        win_rate = 0
    strategy = {
        "total_trades": amount_of_trades,
        "profitable_trades": profitable_trades,
        "losing_trades": losing_trades,
        "total_pnl": round(total_pnl, 2),
        "win_rate": round(win_rate, 2)
    }
    return strategy