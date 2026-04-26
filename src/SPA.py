import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")
df.head()

df["Total"] = df["math score"] + df["reading score"] + df["writing score"]
df["Result"] = df["Total"].apply(lambda x: "Pass" if x >= 120 else "Fail")

pass_rate = (df["Result"] == "Pass").mean() * 100
print("Pass %:", pass_rate)

df[["math score","reading score","writing score"]].mean().plot(kind="bar")
plt.title("Average Scores")
plt.show()

print("Best Subject:", df[["math score","reading score","writing score"]].mean().idxmax())
