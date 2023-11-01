import sqlite3
from MessageDAO import MessageDao
from flask import jsonify
class Message:
    
    def sendMessage(self, req):
        # Call MessageDAO method to perform a soft delete
        success = MessageDao().sendMessage(req)
        if success:
            return jsonify({"message": "Message sent successfully"}), 201
        else:
            return jsonify({"message": "Message not found or failed to send"}), 404

    def deleteMessage(self, m_id):
        # Call MessageDAO method to perform a soft delete
        success = MessageDao().deleteMessage(m_id)
        if success:
            return jsonify({"message": "Message deleted successfully"}), 200
        else:
            return jsonify({"message": "Message not found or failed to delete"}), 404

    def getMessageById(self, m_id):
        Message = MessageDao().getMessageById(m_id)
        if Message:
            return jsonify(Message), 200
        else:
            return jsonify({"Message": "Message not found"}), 404