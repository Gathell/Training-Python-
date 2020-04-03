import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/car/hyundai/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'accept': '*/*'}
HOST = "https://auto.ria.com"
print("начало")

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
print("1OK")

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='address')
    print('2OK')


    cars = []
    for item in items:
        cars.append({
            'title': item.find('span', class_='blue bolt').get_text(strip=True),
            'link': HOST + item.find('a', class_='address').get('href'),
        })
    print(cars)
    print(len(cars))



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('error')

parse()