#import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

#create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

#stemming process
sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'

output = stemmer.stem(sentence)

print(output)
#ekonomi indonesia sedang dalam tumbuh yang bangga

print(stemmer.stem('Mereka meniru - nirukannya'))
#mereka tiru

#pustaka sastrawi bertujuan untuk memberikan hasil stemming yang sederhana dan efisien
#yang menyebabkan beberapa kata diabaikan atau disederhakan. seperti contoh diatas.