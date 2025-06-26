import pandas as pd

coffee = pd.read_csv('./data/coffee.csv')
print(coffee)
print("\n")

df1 = coffee.loc[:, ["Coffee Type", "Units Sold"]]
print(df1)
print("\n")

df2 = coffee.loc[:, ["Day", "Units Sold"]]
print(df2)
print("\n")


df3 = coffee.iloc[0:6, [0, 2]]
print(df3)
print("\n")