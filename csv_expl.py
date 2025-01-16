from main import data, weights, impact
import pandas as pd

df = pd.read_csv('data.csv')
print("got the CSV file")
print("columns found✨: ")
print(df.columns.tolist())

if len(weights) == len(impact) and len(weights) == len(df.columns):
    pass
else:
    raise ValueError("Number of weights, operators, and columns do not match. ", len(weights), len(impact), len(df.columns))


