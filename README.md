# Web scraping first project 🚀

## you just need to delete urls.txt and run in the IDE or Terminal.
## i use pycharm so the .txt will be created in the folder that you work on it.
## after you run please comment this:
```python
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
```
GOOD 
### now you can store all the data in .csv file by runing this:
```py
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
```
## If you like it STAR it ⭐️
