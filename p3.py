from bs4 import BeautifulSoup

html = """
<table>
    <tr><th>Name</th><th>Age</th></tr>
    <tr><td>Alice</td><td>25</td></tr>
    <tr><td>Bob</td><td>30</td></tr>
</table>
"""

soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')

for row in rows:
    cells = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
    print(cells)