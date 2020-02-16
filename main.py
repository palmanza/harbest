import requests
import re
import pandas as pd
import time
import random
from bs4 import BeautifulSoup

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

items = []

for e in range(4):
	page = requests.get('https://www.paginasamarillas.com.ar/b/hoteles/cordoba/p-' + str(e+1) + '/?tieneCobertura=true')
	soup = BeautifulSoup(page.content, 'html.parser')
	rows = soup.findAll("div", {"class": "row"})

	for row in rows:
		emails = re.findall(r"(?<=data-emailcompany=\"\">)(.*?)(?=<\/div>)", str(row))
		companyName = re.findall(r"(?<=data-namecompany=\"\">)(.*?)(?=<\/div>)", str(row))
		city = re.findall(r"(?<=data-bipcity=\"\">)(.*?)(?=<\/div>)", str(row))
		activity = re.findall(r"(?<=data-bipactivity=\"\">)(.*?)(?=<\/div>)", str(row))
		telefono = re.findall(r"(?<=itemprop=\"telephone\">)(.*?)(?=<\/span>)", str(row))

		if emails and companyName and city and activity and telefono and len(emails) == 1 and len(companyName) ==1 and len(city) ==1 and len(activity) ==1 and len(telefono) == 1:
			listedItem = [emails, companyName, city, activity, telefono]
			if not listedItem in items:
				items.append(listedItem)
	time.sleep(random.randint(1,5))
	e+=1
new_df = pd.DataFrame(columns=['Email', 'Nombre', 'Ciudad', 'Actividad', 'Telefono'], data=items)
print(new_df)


