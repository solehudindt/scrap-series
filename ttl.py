from base import simple_get
from bs4 import BeautifulSoup
import urllib3
import logging
import csv

# openf = open('doscom.csv')
with open('doscom.csv', newline='') as f:
		reader = csv.reader(f)
		data = list(reader)

nims = [j for sub in data for j in sub]

def get_birth(x):
	birth = x.split(,)
	return birth[1]

y = list()
for i in nims:
	raw_html = simple_get('http://academic.dinus.ac.id/home/data_mahasiswa/'+i)
	html = BeautifulSoup(raw_html, 'html.parser')

	box = html.find("div", {"class":"col-md-12 panel panel-default"})

	konten = box.find("div", {"class":"col-md-9"})

	x = konten.findAll("td")
	ttl = x[7].text
	birthday = get_birth(ttl)
	y.append(x[7].text)
	logging.info('isi y', y)

print(y)