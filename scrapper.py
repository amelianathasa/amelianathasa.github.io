from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
import urllib.request
import json
from datetime import datetime

now = datetime.now() # current date and time
albumsList = []
i = 1


s = Service('C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://rateyourmusic.com/list/Mr_1337/100_greatest_albums_of_all_time/")

for main in driver.find_elements(By.ID, "user_list"):
	print(main.text.split("\n"))
	for img in main.find_elements(By.TAG_NAME, "img"):
		print(img.get_attribute("src"))
		urllib.request.urlretrieve(img.get_attribute("src"), str(i))
		i = i+1

		albumsList.append({"No": main.text.split("\n")[i], "Artist": main.text.split("\n")[i+1], "Title": main.text.split("\n")[i+3], "Image": img.get_attribute("src"), "WaktuScraping":now.strftime("%Y-%m-%d %H:%M:%S")})



hasil_scrapping = open("hasilScrapping.json", "w")
json.dump(albumsList, hasil_scrapping, indent = 6)
hasil_scrapping.close()

driver.quit()
