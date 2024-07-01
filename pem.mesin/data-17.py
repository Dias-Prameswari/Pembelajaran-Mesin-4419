import pandas as pd 
# data yang format awalnya csv diganti ke xlsx / excell workbook agar bisa run
# datanya juga terlalu banyak 
df = pd.read_excel("data/clean_dataset2.xlsx")
# untuk menampilkan semua data
# pd.set_option('display.max_rows', None)
print(df)