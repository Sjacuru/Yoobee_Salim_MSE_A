import requests
from bs4 import BeautifulSoup
from collections import defaultdict

url = 'https://commeventshub.onrender.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


quotes = soup.find('div', class_='container')
q1 = quotes.find('h2')
q2 = q1.find('span')
q = q2.text.strip()


count_events = q2.text.strip()
print(f"Total upcoming events found: {count_events}")


type_counts = defaultdict(int)
    # Find all divs with the target class
containers = soup.find_all('div', class_='card-body')

for container in containers:
    span = container.find('span', class_='badge bg-info text-dark text-uppercase')
    if span:
        type_name = span.text.strip()
        type_counts[type_name] += 1

    for type_name, count in type_counts.items():
        print(f"{type_name}: {count}")

    

print("total events: "+q)