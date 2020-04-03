import requests
from bs4 import BeautifulSoup
import csv
# pip install beautifulsoup4
# pip install lxml

def get_html(url):
    r = requests.get(url)    # Получим метод Response
    r.encoding = 'utf8'
    return r.text   # Вернем данные объекта text


def csv_read(data):
    with open("data.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['head'], data['link']))

def get_link(html):
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find('div', id='section-content').find_all('a', class_="entry-header")
    for i in head:
        link = 'https://3dnews.ru' + i.get('href')
        heads= i.find('h1').string
        data = {'head': heads,
                 'link': link}
        csv_read(data)
    
data = get_link(get_html('https://3dnews.ru/news'))
#https://3dnews.ru/news