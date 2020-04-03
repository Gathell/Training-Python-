from pathlib import Path
import requests #импортирую библиотеку

BASE_URL = 'https://auto.ria.com/car/hyundai/?page={page_num}' #ссылка которую парсю
BASE_SAVE_PATH = Path('./parser')

for i in range(1 ,4):
    
    r = requests.get(BASE_URL.format(page_num = i))

    print(r.status_code)


    html_file_path = BASE_SAVE_PATH / 'auto_ria_{page_num}.html'.format(page_num = i)

    with open(str(html_file_path.absolute()), 'wb') as f:
        f.write(r.content)
