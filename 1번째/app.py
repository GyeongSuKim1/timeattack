from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient

import jwt, datetime, hashlib

app = Flask(__name__)

client = MongoClient

db = client.db

SECRET_KEY = 'ABCD'


@app.route('/index')
def mypage():
	return render_template('index.html')


@app.route('/')
def signup():
	return render_template('signup.html')


@app.route('/', methods=['POST'])
def api_signup():
	signup_id_receive = request.form['sign_email_give']
	signup_pw_receive = request.form['sign_password_give']

	pw_hash = hashlib.sha256(signup_pw_receive.encode('utf-8')).hexdigest()

	doc = {
		'Eamil': signup_id_receive,
		'password': pw_hash,
	}

	db.user.insert_one(doc)
	return jsonify({'msg': '회원가입 완료!'})

if __name__ == '__main__':
	app.run('0.0.0.0', port=5000, debug=True)
