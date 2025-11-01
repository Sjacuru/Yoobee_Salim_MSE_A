import requests
from bs4 import BeautifulSoup

url = 'https://commeventshub.onrender.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


quotes = soup.find('div', class_='container')
q1 = quotes.find('h2')
q2 = q1.find('span')
q = q2.text.strip()

print("total events: "+q)

