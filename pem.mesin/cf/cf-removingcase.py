# case folding : removing number
# removing number adalah menghapus karakter angka pada kalimat yang sudah ada
# contoh : 
import re
kalimat = "Berikut ini adalah 5 negara dengan pendidikan terbaik di dunia adalah Korea Selatan, Jepang, Singapura, Hong Kong dan Finlandia."
hasil = re.sub(r"\d+", "", kalimat)
print(hasil)
  