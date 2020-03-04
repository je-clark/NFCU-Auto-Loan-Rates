import requests, sys, csv
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt

def get_auto_rates():
	url = "https://www.navyfederal.org/assets/rates/printAutoRatesAll.php"
	
	output = requests.get(url)

	soup = bs(output.text, 'html.parser')
	new_rates_table = soup.find_all("div", class_="table_row clearfix")

	rates = []
	for row in new_rates_table:
		for rate in row.find_all("div", class_="auto_rate"):
			rates.append(rate.get_text())

	return rates

def csv_output(rates):
	filename = r'.\rates.csv'

	with open(filename, 'a+', newline='') as file:
		csv_writer = csv.writer(file)
		csv_writer.writerow([dt.today().strftime("%Y %b %d")] + rates)


rates = get_auto_rates()
csv_output(rates)