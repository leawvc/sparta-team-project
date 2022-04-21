import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%82%BC%EA%B2%B9%EC%82%B4+%EB%A7%9B%EC%A7%91',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

foods = soup.select('#loc-main-section-root > section > div > div.place_section_content > ul > li')

for food in foods:
    a_tag = food.select_one('div._3ZU00 > a:nth-child(1) > div > div > span._3Apve')
    if a_tag is not None:
        title = a_tag.text
        phone = food.select_one('div._3ZU00 > div._1oH7-._1lPUe').text
        ip = food.select_one('div._3ZU00 > div._1B9G6 > div > span > a > span._3hCbH').text

        print(title,phone,ip)