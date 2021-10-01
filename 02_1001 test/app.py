from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

from datetime import datetime

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    today = datetime.now()
    mytime = today.strftime('%Y년%m월%d일 %H:%M:%S')

    doc = {
        'title' : title_receive,
        'content' : content_receive,
        'reg_date' : mytime
    }

    db.timeattack2.insert_one(doc)
    return {"msg": "저장 완료!"}


@app.route('/post', methods=['GET'])
def get_post():
    articles = list(db.timeattack2.find({}, {'_id': False}))
    return jsonify({'all_articles': articles})



@app.route('/post', methods=['DELETE'])
def delete_post():
     return jsonify({'msg': '삭제완료!'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)