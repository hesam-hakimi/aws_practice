from bs4 import BeautifulSoup
import requests
import io

# url = ''.join([''https://twitter.com/search?q=tax', '%',
#               '20software&src=typed_query&f=user''])
res = requests.get(
    'https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films').text
with open('html.html', 'w', encoding='utf-8')as file:
    file.write(res)
soup = BeautifulSoup(res, 'lxml')
match = soup.find_all("table", class_='infobox vevent')

with io.open('html.text', 'w', encoding='utf-8')as file:
    file.write(str(match))
print(match)
