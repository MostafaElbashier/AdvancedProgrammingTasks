import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "no title found"
    print(f"page title: {title}")
else:
    print(f"failed to fetch page. status code: {response.status_code}")