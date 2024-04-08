import pandas as pd 
# datanya terlalu banyak untuk ditampilkan & tdk error 
df = pd.read_csv("data/kamus_clean.csv")
# untuk menampilkan semua data
# pd.set_option('display.max_rows', None)
print(df)