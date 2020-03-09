from base import simple_get
from bs4 import BeautifulSoup
import urllib3

raw_html = simple_get('http://academic.dinus.ac.id/home/data_mahasiswa/A12.2017.05866')

### JakNote
# raw_html = simple_get('https://www.jakartanotebook.com/search?category=0&key=baterai+laptop+lenovo')

# html = BeautifulSoup(raw_html, 'html.parser')

# # for i in html.select('')

# # laptops = html.findAll("div",{"class":"row"})
# laptops = html.findAll("div",{"class":"product-list"})

# for i in laptops:
# 	print(i.div.a["title"])

### Bhineka

# raw_html = simple_get('https://www.bhinneka.com/search?q=laptop')
# html = BeautifulSoup(raw_html, 'html.parser')

# laptops = html.findAll("div",{"id":"catalogueProduct"})

# for i in laptops:
# 	x = i.findAll("div",{"class":"col-lg-3 col-md-4 col-sm-6 bt-product-list"})
# 	for y in x:
# 		one = y.findAll("div",{"div":"bt-product-list-info"})
# 		print(one)

html = BeautifulSoup(raw_html, 'html.parser')

mhs = html.findAll("div", {"class":"col-md-2"})

mahasiwa = list()

for i in mhs[0:29]:
    nama = i.a
    hasil = str(nama.json)
    mahasiwa.append(hasil)

print(mahasiwa)
data = "\t".join(mahasiwa)
kelas = open("kelas.txt", "w")

kelas.write(data)

kelas.close()