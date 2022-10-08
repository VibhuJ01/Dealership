import pandas as pd
df = pd.read_csv("dataset.csv")
print(df['Seats'].value_counts())
print(len(df))
