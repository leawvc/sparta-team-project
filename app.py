import json
import random
import urllib

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

sunny_hot = ['소불고기', '양꼬치', '스파게티', '짜장면', '비빔면', '냉면']
sunny_warm = ['생선구이', '치킨', '돼지두루치기', '카레', '돈까스', '피자', '떡볶이', '닭갈비', '햄버거']
sunny_cool = ['회', '조개탕', '부대찌개', '된장찌개', '수제비', '아구찜']
rain_hot = ['초밥', '쭈꾸미볶음', '돼지국밥', '육회', '족발', '삼계탕']
rain_warm = ['부침개', '라멘', '쌀국수', '규카츠', '마라탕', '삼겹살']
rain_cool = ['조개구이', '김치찌개', '만둣국', '우동', '오뎅탕', '국수']


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


# ## API 역할을 하는 부분
# @app.route('/review', methods=['POST'])
# def write_review():
#     sample_receive = request.form['sample_give']
#     print(sample_receive)
#     return jsonify({'msg': '이 요청은 POST!'})


@app.route('/food/ranking', methods=['GET'])
def read_ranking():
    temper_receive = float(request.args['temper_give'])
    cloud_receive = float(request.args['cloud_give'])
    result = ranking(temper_receive, cloud_receive)

    return jsonify({'ranking': result})




@app.route('/food/location', methods=['GET'])
def get_weather():
    x_receive = request.args['x_give']
    y_receive = request.args['y_give']
    api = "ad941787e755149ec3b3f81c65223d85"

    lon = float(x_receive)
    lat = float(y_receive)

    print(lat, lon)
    units = "metric"
    # api에서 가져온 json을 저장하는 source
    source = urllib.request.urlopen(
        'http://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(
            lon) + '&appid=' + api + '&units=' + units).read()
    # json을 딕셔너리형으로 변환
    list_of_data = json.loads(source)

    temp = list_of_data['main']['temp']
    cloud = list_of_data['clouds']['all']

    return jsonify({'temper': temp , 'cloud': cloud })


@app.route('/food/recommend', methods=['GET'])
def get_recofood():
    temper_receive = float(request.args['temper_give'])
    cloud_receive = float(request.args['cloud_give'])
    result = recofood(temper_receive, cloud_receive)
    print(result)

    return jsonify({'result':result})

def ranking(temper, cloud):
    foodlist = []

    if cloud <= 50:
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

    result = []
    for i in data:
       result.append([i['name'],i['like']])

    return result;

def recofood(temper, cloud):
    foodlist = []

    if cloud == 0:
        if temper >= 20:
            recofood = random.sample(sunny_hot, 3)
            for i in recofood:
                foodlist.append(db.food.find_one({'name': i}))
                data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:3]
        elif temper >= 10:
            recofood = random.sample(sunny_warm, 3)
            for i in recofood:
                foodlist.append(db.food.find_one({'name': i}))
                data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:3]
        else:
            recofood = random.sample(sunny_cool, 3)
            for i in recofood:
                foodlist.append(db.food.find_one({'name': i}))
                data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:3]

    else:
        if temper >= 20:
            recofood = random.sample(rain_hot, 3)
            for i in recofood:
                foodlist.append(db.food.find_one({'name': i}))
                data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:3]
        elif temper >= 10:
            recofood = random.sample(rain_warm, 3)
            for i in recofood:
                foodlist.append(db.food.find_one({'name': i}))
                data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:3]
        else:
            recofood = random.sample(rain_cool, 3)
            for i in recofood:
                foodlist.append(db.food.find_one({'name': i}))
                data = sorted(foodlist, key=(lambda x: x['like']))[::-1][0:3]

    result = []
    for i in data:
        result.append([i['name'], i['img'], i['like']])

    return result






if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
