# case folding : removing punctuation 
# punctuation adalah menghapus karakter tanda baca pada kalimat yang ada
# contoh : 
import string
kalimat = "ini &adalah [contoh] kalimat? {dengan} tanda. baca?!!"
hasil = kalimat.translate(str.maketrans("", "", string.punctuation))
print(hasil)
