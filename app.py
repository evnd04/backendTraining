from user import User
from Message import Message
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/Account', methods=['POST'])
def addNewUser():
    if request.method=='POST':
        return User().addNewUser(request.json)
    else:
        return jsonify("Method not allowed"), 405

@app.route('/Account/getUserByEmail/<email_adress>', methods=['GET'])
def getUserByEmail(email_adress):
    if request.method=='GET':
        return User().getUserByEmail(email_adress)
    else:
        return jsonify("Method not allowed"), 405

@app.route('/Account/getUserById/<user_id>', methods=['GET'])
def getUserById(user_id):
    if request.method=='GET':
        return User().getUserById(user_id)
    else:
        return jsonify("Method not allowed"), 405

@app.route('/Message', methods=['POST'])
def sendMessage():
    if request.method=='POST':
        return Message().sendMessage(request.json)
    else:
        return jsonify("Method not allowed"), 405
    
@app.route('/Message/<int:m_id>', methods=['DELETE'])
def deleteMessage(m_id):
    if request.method=='DELETE':
        return Message().deleteMessage(m_id)
    else:
        return jsonify("Method not allowed"), 405

@app.route('/Message/<int:m_id>', methods=['GET'])
def getMessageById(m_id):
    if request.method=='GET':
        return Message().getMessageById(m_id)
    else:
        return jsonify("Method not allowed"), 405

if __name__=="__main__":
    app.run(debug=True)