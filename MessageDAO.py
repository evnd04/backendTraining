import sqlite3
from flask import Flask, jsonify

def get_db_connection():
        conn = sqlite3.connect("bt.db")
        return conn
    
class MessageDao:
    
    def sendMessage(self, req):
        conn=get_db_connection()
        cursor=conn.cursor()
        query='''INSERT INTO Message (user_id, reply_id, subject, body, date, is_deleted)
                      VALUES (?, ?, ?, ?, datetime('now'), 0)'''
        cursor.execute(query, (req['user_id'], req['reply_id'], req['subject'], req['body'], req['date'], 0))
        conn.commit()
        conn.close()
        
    def deleteMessage(self, m_id):
        query = "UPDATE Message SET is_deleted = 1 WHERE m_id = ?"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (m_id,))
        conn.commit()
        conn.close()
    
    def getMessageById(self, m_id):
        query="SELECT * FROM Message WHERE email_address=?"
        conn = get_db_connection()
        cursor = conn.cursor()
        message=cursor.execute(query, (m_id))
        conn.close()
        return message