import json
from bs4 import BeautifulSoup

content = """<table>
    <thead>
        <th>ID</th>
        <th>Vendor</th>
        <th>Product</th>
    </thead>
    <tr>
        <td>1</td>
        <td>Intel</td>
        <td>Processor</td>
    </tr>
    <tr>
        <td>2</td>
        <td>AMD</td>
        <td>GPU</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Gigabyte</td>
        <td>Mainboard</td>
    </tr>
</table>"""

#with open('in.xml', 'r') as infile:
    #content = infile.read()

soup = BeautifulSoup(content, "lxml")
rows = soup.find_all("tr")

headers = {}

thead = soup.find("thead").find_all("th")

for i in range(len(thead)):
    headers[i] = thead[i].text.strip().lower()

data = []

for row in rows:
    cells = row.find_all("td")
    
    item = {}
    
    for index in headers:
        item[headers[index]] = cells[index].text
    
    data.append(item)

print(json.dumps(data, indent=4))
