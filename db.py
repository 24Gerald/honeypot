import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="password", database="honeypot_db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS attacks (id INT AUTO_INCREMENT PRIMARY KEY, ip VARCHAR(255), payload TEXT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

def log_attack(ip, payload):
    cursor.execute("INSERT INTO attacks (ip, payload) VALUES (%s, %s)", (ip, payload))
    conn.commit()
