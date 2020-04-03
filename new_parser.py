from pprint import pprint
import requests

BASE_URL = 'https://api.hh.ru'

vac_r = requests.get(BASE_URL + 'vacancies')

vacancies = vac_r.json()['items']
first_vac = vacancies[0]

full_vac = requests.get(BASE_URL + 'vacancies' + first_vac['id'])
pprint(full_vac )