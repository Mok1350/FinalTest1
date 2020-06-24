# -*- coding: utf-8 -*-

from __future__ import with_statement
import time
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from contextlib import closing
from flask import Flask,request,session,url_for,redirect,render_template,abort,g,flash
from werkzeug.security import check_password_hash, generate_password_hash

a = None
b = None
c = None
cal = None

word1 =None
word2 =None
word3 =None

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('MINITWIT_SETTINGS',silent=True)

@app.route('/')
def test():
    return render_template('layout.html')

@app.route('/memo1')
def memo1():
    global word1
    return render_template('머신러닝.html',word = word1)


@app.route('/memo2')
def memo2():
    return render_template('정보시스템.html')

@app.route('/memo3')
def memo3():
    return render_template('AI.html')

@app.route('/save',methods=['POST'])
def save():
    global word1
    if 'save' in request.form:
        if request.method == 'POST':
            if request.form['word']!='' :
                word1 = request.form['word']

                return redirect(url_for('memo1'))




@app.route('/sessions')
def sessions(): #지정해준 변수(a,b,c,cal)에 담긴 값을 연산하는 함수
    """calculator"""
    global a
    global b
    global c
    global cal

    if a is not None and b is not None:
        if cal=='+':
            c = str(float(a) + float(b))
        elif cal == '-':
            c = str(float(a) - float(b))
        elif cal == '*':
            c = str(float(a) * float(b))
        elif cal == '/':
            c = str(float(a) / float(b))
        else:
            cal = None
    return render_template('sessions.html', num=a ,num2=b, num3=c, cal=cal)

@app.route('/calculate2',methods=['POST'])
def calculate2(): #우리가 입력한 값을 지정해 준 변수(a,b,c,cal)에 담는 함수
    global a
    global b
    global cal

    if 'plus' in request.form:
        cal = '+'
    elif 'minus' in request.form:
        cal = '-'
    elif 'mul' in request.form:
        cal = '*'
    elif 'div' in request.form:
        cal = '/'
    else:
        cal = None

    if request.method == 'POST':
        if request.form['num']!='' and request.form['num2']!='':
            a = request.form['num']
            b = request.form['num2']
            return redirect(url_for('sessions'))
        else:
            a = request.form['num']
            b = request.form['num2']
            if a =='':
                if b =='':
                    a = None
                    b = None
                else:
                    a = None
            else:
                b = None
            return redirect(url_for('sessions'))



#작성된 코드 실행
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)