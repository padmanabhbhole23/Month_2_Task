import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

df = pd.read_csv("SuperMarket Analysis.csv")
df.head()

print(df.shape)
print(df.info())
print(df.describe())

product_sales = df.groupby("Product line")["Sales"].sum().sort_values()

product_sales.plot(kind="barh", title="Sales by Product Line")
plt.show()

df["Date"] = pd.to_datetime(df["Date"])
daily_sales = df.groupby("Date")["Sales"].sum()

plt.plot(daily_sales)
plt.title("Daily Sales Trend")
plt.show()

print("Top Product:", product_sales.idxmax())
print("Total Revenue:", df["Sales"].sum())