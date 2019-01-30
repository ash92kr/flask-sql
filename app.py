from flask import Flask, render_template
from datetime import datetime, timedelta

import os
app = Flask(__name__)   # 인스턴스 만들기

@app.route('/')
def index():
    return 'hello there!'

# 5월 20일부터 d-day 카운트 출력하기
@app.route('/dday')
def dday():
    day = datetime(2019, 5, 20) - datetime.today()
    return f'{day.days}일 남았습니다.'
# https://docs.python.org/2/library/datetime.html#datetime.timedelta
# today = datetime.datetime.now()
# vacation = datetime.datetime(2019, 5, 20)
# td = vacation - today


# variable routing
# @app.route('/hi/<string:name>')
# def hi(name):   # 주소에 있는 것을 매개변수로 받아옴
#     return f'안녕, {name}'


@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number ** 3}입니다.'


# render template
# @app.route('/hi/<string:name>')
# def greeting(name):
#     # greeting.html로 위처럼 안녕 ~~를 출력하기
#     return render_template('greeting.html', html_name=name)
  
  
# if문
@app.route('/hi/<string:name>')
def greeting(name):
    # greeting.html로 위처럼 안녕 ~~를 출력하기
    return render_template('greeting.html', html_name=name)  


# for문
@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한타인']
    return render_template('movie.html', movies=movies)
    

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)   # 자동으로 다른 환경에서 IP를 찾아줌