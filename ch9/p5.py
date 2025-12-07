from bs4 import BeautifulSoup
import csv

html = """
<ul>
    <li>Apple</li>
    <li>Banana</li>
    <li>Cherry</li>
</ul>
"""

soup = BeautifulSoup(html, 'html.parser')
fruits = [li.get_text(strip=True) for li in soup.find_all('li')]

with open('fruits.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Fruit'])  
    for fruit in fruits:
        writer.writerow([fruit])

print("Saved to fruits.csv")