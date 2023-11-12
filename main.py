import requests
from bs4 import BeautifulSoup
import lxml

def get_cashbacks(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	cashback_info = soup.select('.shop-info')
	for info in cashback_info:
		shop_name = info.select_one('.name a').text
		cashback = info.find('span', {'class':'percent'}).text.split('%')[0]
		yield shop_name, float(cashback)

cashback_urls = ['https://cash-backer.club' for _ in range(5)]

for url in cashback_urls:
	print(url)

	for name, cashback in get_cashbacks(url):
		print(f' {name} {cashback}')


