import pandas as pd 
# datanya terlalu banyak untuk ditampilkan & tdk error 
df = pd.read_csv("data/Dataset_Sentimen_Emosi.csv")
# untuk menampilkan semua data
# pd.set_option('display.max_rows', None)
print(df)