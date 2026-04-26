import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("AAPL.csv")
df.head()
df["MA_5"] = df["Close"].rolling(5).mean()
plt.plot(df["Close"], label="Close")
plt.plot(df["MA_5"], label="MA 5")
plt.legend()
plt.title("Stock Price Trend")
plt.show()
returns = df["Close"].pct_change().mean()
print("Avg Return:", returns)
