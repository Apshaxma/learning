import pandas as pd

print("hello world ")

data = pd.read_csv("train.csv")
print(data.head())

data.isna().sum()