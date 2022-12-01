# Web scraping is used for extracting data from websites
from ast import ClassDef
import requests
from bs4 import BeautifulSoup

# Page this code's going to take data from
url = 'https://www.espn.com/nba/standings'

# HTTP headers are used to transfer data between a Web server and a client
headers = {'User-Agent': 'Mozilla/5.0'} 
response = requests.get(url , headers=headers)

# If the 'response.status_code' is equal to 200 you are able to make requests
soup = BeautifulSoup(response.content,'html.parser')

stat_table = soup.find_all('table', class_ = 'Table Table--align-right Table--fixed Table--fixed-left')

# Converting 'stat_table' from a resultset to a table
stat_table = stat_table[0]

print(stat_table)

# Looping to get all the table infos
for row in stat_table.find_all('tr'):
    for cell in row.find_all('td'):
        print(cell.text)
    
print(len(stat_table))

# Write all this information in a .txt file
with open ('info.txt', 'w') as r:
    for row in stat_table.find_all('tr'):
        for cell in row.find_all('td'):
            r.write(cell.text)