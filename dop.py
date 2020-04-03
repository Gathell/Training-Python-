import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://auto.ria.com/car/hyundai/?page={page_num}'

r = requests.get(BASE_URL)

soap = BeautifulSoup(r.text, "html.parser")

print(soap.title)

msgs = soap.select('div.content')
# print(len(msgs))
# print(msgs[-1])

parsed_msgs = []

for msg in msgs:
    txt = msg.get_text()
    parsed_msgs.append(txt)

print(len(parsed_msgs))
print(parsed_msgs[1])