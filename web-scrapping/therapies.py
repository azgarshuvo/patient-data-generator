from bs4 import BeautifulSoup
import requests
import json

dicts = {}
values = []

def therap():
    html_texts = requests.get('https://en.wikipedia.org/wiki/List_of_therapies').text
    soup = BeautifulSoup(html_texts, 'lxml')

    therapy_data = soup.find('div', class_ = 'div-col')
    therapies = therapy_data.find_all('li')

    for therapy in therapies:
        theraphy_name = therapy.get_text()
        if theraphy_name not in '':
            values.append(theraphy_name)

    for i in range(len(values)):
        dicts[i] = values[i]

    json_object = json.dumps(dicts, indent = 4)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

print(therap())








