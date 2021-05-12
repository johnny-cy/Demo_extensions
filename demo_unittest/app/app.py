from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

# app, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ubuntu/demo/src/demo_unittest/tests/db'

db = SQLAlchemy(app)

# model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# refresh tables
db.drop_all()
db.create_all()

# apis
@app.route("/add_user")
def add_user():
    name = request.args.get('name')
    if User.query.filter_by(username=name).first() is None:
        user = User(username=name)
        db.session.add(user)
        db.session.commit()
        return jsonify({"add": name, "status": "success"})
    else:
        return jsonify({"add": '', "status":"already exists"})

@app.route("/user_info")
def user_info():
    users = db.session.query(User.id, User.username)
    user_info = [u._asdict() for u in users]
    return jsonify({"user_info": user_info})

@app.route("/delete_user")
def delete_user():
    try:
        name = request.args.get('name')
        user = User.query.filter_by(username=name).one()
        db.session.delete(user)
        db.session.commit()
        return jsonify({"delete": name, "status": "success"})
    except:
        return jsonify({"delete": '', "status": "user not found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)