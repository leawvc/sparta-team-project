import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.diningcode.com/isearch.php?query=서초구+갈비',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

foods = soup.select('#div_normal > ul > li')

result = []

for food in foods:
    a_tag = food.select_one('a > span.btxt')
    if a_tag is not None:
        title = a_tag.text
        image = food.select_one('a > div').attrs['style'].split(';')[1].strip().split('\'')[1]
        kind = food.select_one('a > span.stxt').text
        ip = food.select_one('a > span.ctxt').text

        result.append({'image':image, 'title':title.strip(), 'kind': kind, 'ip':ip})


print(result)
