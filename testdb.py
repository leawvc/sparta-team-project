import random
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


#지역: 강남구, 날씨: 비, 기온: 따뜻함 가정

#온도 - 20도 이상: 더움, 19~10도: 따뜻함 9도 이하: 추움
#날씨 - 맑음 비

#맑음 and 더움

weather = 1;
temper = 25;


sunny_hot = ['소불고기','양꼬치','스파게티', '짜장면', '비빔면', '냉면']
sunny_warm = ['생선구이','치킨', '돼지두루치기', '카레', '돈까스', '피자', '떡볶이', '닭갈비', '햄버거']
sunny_cool = ['회', '조개탕', '부대찌개', '된장찌개', '수제비', '아구찜']
rain_hot = ['초밥', '쭈꾸미볶음', '돼지국밥', '육회', '족발', '삼계탕']
rain_warm = ['부침개', '라멘', '쌀국수', '규카츠', '마라탕', '삼겹살']
rain_cool = ['조개구이','김치찌개', '만둣국', '우동', '오뎅탕', '국수']

foodlist = []
#
# if weather == 0:
#     if temper >= 20:
#         recofood = random.sample(sunny_hot, 3)
#     elif temper >= 10:
#         recofood = random.sample(sunny_warm, 3)
#     else:
#         recofood = random.sample(sunny_cool, 3)
#
# else:
#     if temper >= 20:
#         recofood = random.sample(rain_hot, 3)
#     elif temper >= 10:
#         recofood = random.sample(rain_warm, 3)
#     else:
#         recofood = random.sample(rain_cool, 3)
#-----------------------------------------------

if weather <= 50:
    if temper >= 20:
        for i in sunny_hot:
            foodlist.append(db.food.find_one({'name': i}))
            data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:5]

    elif temper >= 10:
        for i in sunny_warm:
            foodlist.append(db.food.find_one({'name': i}))
            data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:5]
    else:
        for i in sunny_cool:
            foodlist.append(db.food.find_one({'name': i}))
            data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:5]

else:
    if temper >= 20:
        for i in rain_hot:
            foodlist.append(db.food.find_one({'name': i}))
            data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:5]


    elif temper >= 10:
        for i in rain_warm:
            foodlist.append(db.food.find_one({'name': i}))
            data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:5]
    else:
        for i in rain_cool:
            foodlist.append(db.food.find_one({'name': i}))
            data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:5]

for i in data:
    img = i['img']
    name = i['name']
    like = i['like']
    print('img: ', img, 'name: ' ,  name,'like: ', like)
