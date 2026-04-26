import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("weatherHistory.csv")
df.head()
df["Formatted Date"] = pd.to_datetime(df["Formatted Date"], utc=True)
df.set_index("Formatted Date", inplace=True)

df["Temperature (C)"].resample("ME").mean().plot()
plt.title("Monthly Avg Temperature")
plt.show()
df["Humidity"].hist()
plt.title("Humidity Distribution")
plt.show()
print("Avg Temp:", df["Temperature (C)"].mean())
print("Max Temp:", df["Temperature (C)"].max())
