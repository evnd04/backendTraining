import sqlite3

#connect to a database
conn= sqlite3.connect("bt.db")

#create a cursor
cursor = conn.cursor()


# Create tables
query = """
CREATE TABLE Account ( user_id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    date_of_birth TEXT,
                    gender TEXT,
                    phone_number TEXT,
                    email_address TEXT,
                    password TEXT,
                    is_premium BOOLEAN,
                    is_deleted BOOLEAN
                );
"""
cursor.execute(query)


cursor.execute('''CREATE TABLE Message(
                    m_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    reply_id INTEGER,
                    subject TEXT,
                    body TEXT,
                    date TEXT,
                    is_deleted BOOLEAN,
                    FOREIGN KEY (user_id) REFERENCES Account(user_id),
                    FOREIGN KEY (reply_id) REFERENCES Message(m_id)
                );''')


cursor.execute('''CREATE TABLE Recipient(
                    m_id INTEGER,
                    user_id INTEGER,
                    category TEXT,
                    is_read BOOLEAN,
                    is_deleted BOOLEAN,
                    PRIMARY KEY(m_id, user_id),
                    FOREIGN KEY (user_id) REFERENCES Account(user_id),
                    FOREIGN KEY (m_id) REFERENCES Message(m_id)
                );''')


# Commit the changes and close the connection
conn.commit()
conn.close()