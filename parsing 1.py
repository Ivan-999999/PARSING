import requests
from bs4 import BeautifulSoup
import csv
# Ниже идут константы, которые можно запрашивать через input.
CSV = 'cards.csv'
HOST = 'https://minfin.com.ua/' # Домен, который парсим
URL = 'https://minfin.com.ua/cards/' # Страница, которую будете парсить
# Чтобы сайт не подумал, что я бот, пробрасываем подзаголовки в следующей константе
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

# Собираем нужную информацию с одной страницы.
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-item')
    cards = []
# ниже данные, которые мы хотим забрать.
    for item in items:
        cards.append(
            {
                'title':item.find('div', class_='title').get_text(strip=True),
                'link_product': HOST + item.find('div', class_='title').find('a').get('href'),
                'brand': item.find('div', class_='brand').get_text(strip=True),
                'card_img': HOST + item.find('div', class_='image').find('img').get('src')
            }
        )
    return cards

# теперь нужна функция, которая будет последовательно запускать наш код.

def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название продукта', 'Ссылка на продукт', 'Банк', 'Изображение карты'])
        for item in items:
            writer.writerow( [item['title'], item['link_product'], item['brand'], item['card_img']])


def parser(PAGENATION):
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION + 1):
            print(f'Парсим страницу: {page}')
            html = get_html(URL, params={'page' : page})
            cards.extend(get_content(html.text))
            save_doc(cards, CSV)
        pass
    else:
        print('Error')

# parser()






