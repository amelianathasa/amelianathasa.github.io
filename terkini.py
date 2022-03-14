#import package request dan Beautiful Soup 
import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

#Request ke website yang akan discrap 
page = requests.get("https://republika.co.id/")
now = datetime.now() # current date and time


#extract konten pada web menjadi object BeautifulSoup 
obj = BeautifulSoup(page.text, 'html.parser')

for conten_kanal in obj.find_all('div', class_ = 'teaser_conten1_center'):
	print(conten_kanal.find('h1').text)
	print(conten_kanal.find('h2').text)
	print(obj.find('div', class_ = 'date').text)


# memasukkan kedalam file .txt
f = open('C:\\xampp\\htdocs\\scraping\\terkini.txt', 'w')
for conten_kanal in obj.find_all('div', class_ = 'teaser_conten1_center'):
	f.write(conten_kanal.find('h1').text)
	f.write(conten_kanal.find('h2').text)
	f.write(obj.find('div', class_ = 'date').text)
	# f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
	f.write('\n')
f.close()


#Memasukkan data dalam fil json 
#Deklarasi list kosong 
data=[]

#lokasi file json 
f = open('C:\\xampp\\htdocs\\scraping\\terkini.json', 'w')
for conten_kanal in obj.find_all('div', class_ = 'teaser_conten1_center'):
	# append terkini ke variabel data 
	data.append({"Judul": conten_kanal.find('h2').text,"Kategori": conten_kanal.find('h1').text, "WaktuPublish": obj.find('div', class_ = 'date').text, "WaktuScraping":now.strftime("%Y-%m-%d %H:%M:%S")})
	


#dump list dictionary menjadi json
jdumps = json.dumps(data)
f.writelines(jdumps)
f.close()
