from base import simple_get
from bs4 import BeautifulSoup
import urllib3

# link = simple_get('http://academic.dinus.ac.id/home/daftar_mahasiswa_perjadwal/.{}')
link = 'http://academic.dinus.ac.id/home/daftar_mahasiswa_perjadwal/.{}'


start = 153151
stop = 153156

mahasiwa = list()

for idx in range(start, stop):
	page = urllib3.PoolManager()
	res = page.request('GET', link)
	html = BeautifulSoup(res.data, 'html.parser')
	mhs = html.findAll("div", {"class":"col-md-2"})	
	
	for i in mhs[0:29]:
		nama = i.a
		mahasiwa.append(nama)

hasil = "\t".join(mahasiwa)

kelas = open("kelas.txt", "w")
kelas.write(hasil)
kelas.close()

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