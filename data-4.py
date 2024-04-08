import pandas as pd 
# datanya terlalu banyak untuk ditampilkan 
df = pd.read_csv("data/train.csv")
# untuk menampilkan semua data
# pd.set_option('display.max_rows', None)
print(df)