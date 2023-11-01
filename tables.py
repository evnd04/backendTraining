import mysql.connector

# Connect to a MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Led%2002',
        database='backend'
    )
    return conn

conn = get_db_connection()
cursor= conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Account (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_of_birth DATE,
    gender VARCHAR(10),
    phone_number VARCHAR(15),
    email_address VARCHAR(255),
    password VARCHAR(255),
    is_premium BOOLEAN,
    is_deleted BOOLEAN
);
""")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Message (
    m_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    reply_id INT,
    subject VARCHAR(255),
    body TEXT,
    date DATETIME,
    is_deleted BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES Account(user_id),
    FOREIGN KEY (reply_id) REFERENCES Message(m_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Recipient (
    m_id INT,
    user_id INT,
    category VARCHAR(50),
    is_read BOOLEAN,
    is_deleted BOOLEAN,
    PRIMARY KEY(m_id, user_id),
    FOREIGN KEY (user_id) REFERENCES Account(user_id),
    FOREIGN KEY (m_id) REFERENCES Message(m_id)
);
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
