from bs4 import BeautifulSoup
import requests
from langdetect import detect  # Для проверки языка


news = []
def poisk(zapros):  #  zapros =  'facebook'
    global news
    news = []
    URL = f'https://ru.investing.com/search/?q={zapros}&tab=news'
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
               'accept': '*/*'}
    HOST = 'https://ru.investing.com'

    r = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.find_all('div', class_='articleItem')

    news = []
    for x in name:
        url_news = x.find('a').get('href')  # Получаем ссылку из новостей
        if detect(x.text.strip()) == 'ru':
            news.append(x.text.strip() + '\n'+ HOST + url_news)
        else:
            continue