from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta



#지역: 강남구, 날씨: 비, 기온: 따뜻함 가정

