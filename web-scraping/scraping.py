from bs4 import BeautifulSoup
import requests

html_texts = requests.get('https://belancer.com/projects').text
soup = BeautifulSoup(html_texts, 'lxml')
job = soup.find('div', class_ = 'span13-sm')

job_title = job.find('h4', class_ = 'no-mar').a.span.text
posted_on = job.find('span', class_= 'show').span.text
budget = job.find('span', class_= 'c cr').text
print(f''' 

Job Title: {job_title}
Posted On: {posted_on}
Budget: {budget}

''')