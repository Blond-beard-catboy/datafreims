import pandas as pd

pd.set_option('display.max_rows', 20)      # Максимум строк
pd.set_option('display.max_columns', 20)    # Максимум столбцов
pd.set_option('display.width', 100)        # Ширина вывода

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'], index=['x', 'y', 'z'])
print(df)
print("--------------------------------")
print(df.describe())