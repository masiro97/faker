# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import random
import csv
from faker import Faker

app = Flask(__name__)

fake = Faker('ko_Kr')

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/result")
def result():
    # 1. "/" 날아온 이름 두개를 가져온다.
    # 2. 궁합을 구라친다. (50 ~ 100 사이의 숫자를 랜덤하게 뽑는다)
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    goonghap = random.randrange(50,101)
    # names라는 배열에 입력된 두 이름을 넣는다. -> file write해서 csv에 저장
    print(name1)
    print(name2)
    f = open('names.csv','a')
    print(f)
    writer = csv.writer(f)
    writer.writerow([name1, name2, goonghap])
    f.close()
    return render_template('result.html', name1 = name1, name2 = name2, goonghap = goonghap)

@app.route("/admin")
def admin():
    # names에 들어가 있는 모든 이름을 출력한다.
    f = open('names.csv', 'r')
    names = csv.reader(f)
    return render_template('admin.html', names=names)

@app.route("/ffaker")
def ffaker():

    name = fake.name()
    address = fake.address()
    text = fake.text()
    return render_template('ffaker.html', name=name, address=address, text=text)
    
app.run(host='0.0.0.0', port='8080', debug=True)