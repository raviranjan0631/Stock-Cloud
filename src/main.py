import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

data = dict()
data['news_headlines'] = []
data['post_date'] = []
data['news_summary'] = []
data['news_link'] = []
data['news_content'] = []

# selenium
# print(extract_news('https://www.moneycontrol.com/news/photos/business/stocks/bajaj-auto-tata-motors-among-7-stocks-forming-golden-cross-pattern-heres-what-it-means-6070421.html'))

url = 'https://www.moneycontrol.com/news/business/markets/'
# url = 'https://www.moneycontrol.com/news/business/stocks/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


ul_tags = soup.find_all('ul', {'id':'cagetory'})

li_tags = ul_tags[0].find_all('li')

def extract_news(link_article):
    response = requests.get(link_article)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('div', {'id': 'article-main'})
    paragraphs = ''
    
    if len(news) > 0:
        news = news[0]
        p_tags = news.find_all('p')
        
        for p in p_tags:
            paragraphs += p.text + '\n'
    
    return paragraphs


for li in li_tags:
    if len(li.text.strip()) >= 1:
        a = li.find_all('a')[0]
        p = li.find_all('p')[0]
        span = li.find_all('span')[0]
        date = span.text.replace('IST', '')
        article_text = extract_news(a['href'])
        data['news_headlines'].append(a['title'])
        data['post_date'].append(date)
        data['news_summary'].append(p.text)
        data['news_link'].append(a['href'])
        data['news_content'].append(article_text)


data = pd.DataFrame(data) 
# df = pd.append([data, df], axis = 1)
data.to_csv('./data/news.csv', index = False) 
        
