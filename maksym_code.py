def clean_data(df):
    df=df.dropna()
    df = df.drop_duplicates()
    df = df.sort_index()
    return df
def calculate_moving_average(df):
    df["Short_MA"]=df["Close"].rolling(window=20).mean()
    df["Long_MA"]=df["Close"].rolling(window=50).mean()
    df.dropna()
    return df
def signals(df):
    df["Signal"] = "Hold"
    for i in range(1, len(df)):
        today_short=df.iloc[i]["Short_MA"]
        today_long=df.iloc[i]["Long_MA"]
        yesterday_short=df.iloc[i-1]["Short_MA"]
        yesterday_long=df.iloc[i-1]["Long_MA"]
        # for signal "BUY"
        if today_short>today_long and yesterday_short<=yesterday_long:
            df.loc[df.index[i], "Signal"] = "BUY"
        elif today_short<today_long and yesterday_short>=yesterday_long:
            df.loc[df.index[i], "Signal"] = "SELL"
    return df

