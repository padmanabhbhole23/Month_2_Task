import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid_19_clean_complete.csv")

# Convert Date properly
df["Date"] = pd.to_datetime(df["Date"])

# Print preview (IMPORTANT)
print(df.head())

# Global cases over time
global_cases = df.groupby("Date")["Confirmed"].sum()

# Plot properly
plt.figure(figsize=(10,5))
plt.plot(global_cases)
plt.title("Global COVID Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.show()

# Top countries
top = df.groupby("Country/Region")["Confirmed"].max().sort_values(ascending=False).head(5)
print("\nTop 5 Countries:\n", top)

# Total cases
print("Total Cases:", df["Confirmed"].max())