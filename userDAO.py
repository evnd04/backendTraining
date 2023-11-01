from tables import get_db_connection
from flask import Flask, jsonify

app = Flask(__name__)
class UserDAO:

    def addNewUser(self, user_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = query = "INSERT INTO Account (first_name, last_name, date_of_birth, gender, phone_number, email_address, password, is_premium, is_deleted) VALUES (%s, %s, STR_TO_DATE(%s, '%c-%d-%y'), %s, %s, %s, %s, 0, 0)"
        values = (user_data['first_name'], user_data['last_name'], user_data['date_of_birth'], user_data['gender'], user_data['phone_number'], user_data['email_address'], user_data['password'])
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        return True

    def getUserByEmail(self, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Account where email_address = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        conn.close()
        return user

    def getUserById(self, id):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Account where user_id = %s"
        cursor.execute(query, (id,))
        user = cursor.fetchone()
        conn.close()
        return user

if __name__ == '__main__':
    app.run()
