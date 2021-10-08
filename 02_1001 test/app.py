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

    count = db.articles.count()
    # 게시글 삭제시 중복 가능 ->   존재하는  number +1 로 바꿔야함
    if count == 0:
        count = 1
    elif count > 0:
        count = count + 1

    doc = {
        'idx': count,
        'title': title_receive,
        'content': content_receive,
        'reg_date': mytime
    }

    db.timeattack2.insert_one(doc)
    return {"msg": "저장 완료!"}


@app.route('/post', methods=['GET'])
def get_post():
    articles = list(db.timeattack2.find({}, {'_id': False}))
    return jsonify({'all_articles': articles})



@app.route('/post', methods=['DELETE'])
def delete_post():
    idx_receive = request.form['idx']

    db.timeattack2.delete_one({'idx': idx_receive})
    return jsonify({'msg': '삭제완료!'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)