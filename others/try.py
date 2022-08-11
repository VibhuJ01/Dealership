import pandas as pd
df = pd.read_csv("dataset.csv")
print(df['Seats'].value_counts())
df = df.dropna()
print(len(df))
