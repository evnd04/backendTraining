import sqlite3
from user import User
from Message import Message
from flask import Flask, request, jsonify

conn= sqlite3.connect("bt.db")
cursor=conn.cursor()

app = Flask(__name__)

@app.route('/Account', methods=['POST'])
def addNewUser(self):
    if request.method=="POST":
        details= request.json()
        return User().addNewUser(details)
    else:
        return jsonify("Method not allowed"), 405

@app.route('/Account/<int:email_adress>', methods=['GET'])
def getUserByEmail(self, email_adress):
    if request.method=="GET":
        return User().getUserByEmail(email_adress)
    else:
        return jsonify("Method not allowed"), 405

@app.route('/Account/<int:user_id>', methods=['GET'])
def getUserById(self, user_id):
    if request.method=="GET":
        return User().getUserById(user_id)
    else:
        return jsonify("Method not allowed"), 405

@app.route('/Message', methods=['POST'])
def sendMessage(self):
    if request.method=="POST":
        req=request.json()
        return Message().sendMessage(req)
    else:
        return jsonify("Method not allowed"), 405
    
@app.route('/Message/<int:m_id>', methods=['DELETE'])
def deleteMessage(self, m_id):
    if request.method=="DELETE":
        return Message().deleteMessage(m_id)
    else:
        return jsonify("Method not allowed"), 405

@app.route('/Message/<int:m_id>', methods=['GET'])
def getMessageById(self, m_id):
    if request.method=="GET":
        return Message().getMessageById(m_id)
    else:
        return jsonify("Method not allowed"), 405