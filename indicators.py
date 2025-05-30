import pandas as pd
import pandas_ta as ta

def get_rsi_signal(price_data, period=14):
    df = pd.DataFrame(price_data, columns=["close"])
    df["rsi"] = ta.rsi(df["close"], length=period)
    if df["rsi"].iloc[-1] < 30:
        return "BUY"
    elif df["rsi"].iloc[-1] > 70:
        return "SELL"
    else:
        return "HOLD"
      
