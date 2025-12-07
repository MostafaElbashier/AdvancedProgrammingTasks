import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    
    if links:
        for link in links:
            href = link['href']
            print(href)
    else:
        print("no links found.")
else:
    print(f"failed to fetch page. status code: {response.status_code}")