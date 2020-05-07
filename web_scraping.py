import requests
from bs4 import BeautifulSoup
import lxml
import time
__doc__
# source : http://example.webscraping.com/
# learned and apply with an youtube video
'''
example: 
soup = BeautifulSoup(response.text, 'lxml') 
title = soup.find('title') => find the element and whats in
print(title) => give the <title>blablabla</title>
print(title.text) => give only the content of html element
tds = soup.findAll('td') => give all the td 
print(len(tds)) => give the number of td element in the html file
'''
# <td>
#   <div>
#       <a href="/places/default/view/Antigua-and-Barbuda-10">
#       <img src="/places/static/images/flags/ag.png"/>Antigua and Barbuda</a>
#   </div>
# </td>

links = []
for i in range(26):
    url = 'http://example.webscraping.com/places/default/index/' + str(i)
    response = requests.get(url)
    print(response)
    if response.ok:
        print('Page:' + str(i))
        soup = BeautifulSoup(response.text, 'lxml')
        tds = soup.findAll('td')
        for td in tds:
            a = td.find('a')
            link = a['href']
            links.append('http://example.webscraping.com' + link)
        time.sleep(2)

print(len(links))
with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link + "\n")

'''
with open('urls.txt', 'r') as inf:
    with open('pays.csv', 'w') as outf:
        outf.write('pays, \t\t\t\t population\n')
        for row in inf:
            url = row.strip()
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.text, 'lxml')
                country = soup.find('tr', {'id': 'places_country__row'}).find('td', {'class': 'w2p_fw'})
                pop = soup.find('tr', {'id': 'places_population__row'}).find('td', {'class': 'w2p_fw'})
                print('Pays: ' + country.text + ' Pop: ' + pop.text)
                outf.write(country.text + ',' + '\t' + '\t' + '\t' + pop.text.replace(',', '') + '\n')
            time.sleep(1)
'''
