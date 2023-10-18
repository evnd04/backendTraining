import sqlite3
from flask import Flask, jsonify

def get_db_connection():
        conn = sqlite3.connect("bt.db")
        return conn
    
class UserDAO:

    def addNewUser(self, user_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        query="INSERT INTO Account (first_name, last_name, date_of_birth, gender, phone_number, email_address, password, is_premium, is_deleted) VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0)"
        cursor.execute(query, (user_data['first_name'], user_data['last_name'], user_data['date_of_birth'], user_data['gender'], user_data['phone_number'], user_data['email_address'], user_data['password']))
        conn.commit()
        conn.close()
        return True
        
    def getUserByEmail(self,email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Account where email_address=?", email)
        user=cursor.fetchone()
        conn.close()
        return user

    def getUserById(self, id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Account where user_id=?", id)
        user=cursor.fetchone()
        conn.close()
        return user
