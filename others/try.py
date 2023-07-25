

import pandas as pd
df = pd.read_csv("dataset.csv")
print(df['Seats'].value_counts())
print(len(df))
df.loc[len(df.index)] = [0000,'Amy', 89, 93,2435,'P','M',567,4567,456,5] 
print(df.loc[df.index == 19999])
print(len(df))
