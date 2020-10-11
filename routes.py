#-*- coding: UTF-8 -*-
#!/usr/bin/env python
from flask import jsonify
import os, sys,json
from PIL import Image as img
from flask import request
def img2data(img):
    image = Image.open(img)
    return list(image.load())

from app import app
@app.route('/')
@app.route('/api')
def index():
    return "hello world"data
# api получаем картинку оправляем data
@app.route("/api/cars")
def get_car():
    im = request.data()
    #data = img2data(img)
    returm json.dump(data)

@app.route('/api/marketplace')
def get_marketpalce():
    pass

