from tables import get_db_connection
from flask import Flask, jsonify
import mysql.connector
class MessageDao:
    def sendMessage(self, req):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = '''INSERT INTO Message (user_id, reply_id, subject, body, date, is_deleted)
                   VALUES (%s, %s, %s, %s, NOW(), 0)'''
        data = (req['user_id'], req['reply_id'], req['subject'], req['body'])
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        return True

    def deleteMessage(self, m_id):
        query = "UPDATE Message SET is_deleted = 1 WHERE m_id = %s"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (m_id,))
        affected_rows = cursor.rowcount 
        conn.commit()
        conn.close()

        if affected_rows > 0:
            return True  
        else:
            return False  


    def getMessageById(self, m_id):
        query = "SELECT * FROM Message WHERE m_id = %s"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (m_id,))
        message = cursor.fetchone()
        conn.close()
        return message
