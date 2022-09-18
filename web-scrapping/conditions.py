from bs4 import BeautifulSoup
import requests
import json

dicts = {}
values = []

def condition():
    html_texts = requests.get('https://www.nhsinform.scot/illnesses-and-conditions/a-to-z').text
    soup = BeautifulSoup(html_texts, 'lxml')

    deasease_data = soup.find_all('h2', class_ = 'module__title')
    
    for desease in deasease_data:
        desease_name = desease.get_text().replace(' ','').replace('\r\n\t\t', '').replace('\r\n\t','')
        if desease_name not in '':
            values.append(desease_name)

    for i in range(len(values)):
        dicts[i] = values[i]

    return json.dumps(dicts)

print(condition())