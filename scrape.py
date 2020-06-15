import requests
from bs4 import BeautifulSoup
import json

for i in range(0, 483,7):
    html = "http://agronews.uz/ru/news?start="
    response = requests.get(html + str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find('div', class_='blog').find_all('div', class_='item column-1')
    data = {}
    for post in news:
        title = post.find('h2').text.strip()
        date = post.find('dd',class_='published').text.strip()
        url = 'http://agronews.uz'+post.find('h2').find('a').get('href')
        smallInfo = post.find('span').text
        body = requests.get(url)
        inner_soup = BeautifulSoup(body.text, 'html.parser')
        article = inner_soup.find('span').text
        data = {
            'title': title,
            'date': date,
            'url': url,
            'smallInfo': smallInfo,
            'article': article
        }
        with open('data.json', 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)