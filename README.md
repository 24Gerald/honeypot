# Honeypot and Threat Intelligence Collection System

## Overview
This project is a **Honeypot and Threat Intelligence Collection System** that helps capture and analyze malicious attacks. It uses **Python, SQL, HTML5, JavaScript, and Bash** to simulate vulnerable services, log attack attempts, and provide a dashboard for visualization.

## Features
- **Fake SSH & HTTP Honeypot**: Captures attack attempts and logs data.
- **Database Logging**: Stores attack details in MySQL/PostgreSQL.
- **Threat Intelligence**: Checks attacker IPs with external APIs (AbuseIPDB, VirusTotal).
- **Web Dashboard**: Displays attack logs using Flask and JavaScript.
- **Automation & Alerts**: Sends notifications and blocks malicious IPs automatically.

## Technologies Used
- **Backend**: Python (Flask, Paramiko, Requests, MySQL Connector)
- **Frontend**: HTML5, JavaScript (Chart.js, Fetch API)
- **Database**: MySQL/PostgreSQL
- **Scripting**: Bash for automation

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/honeypot-threat-intel.git
cd honeypot-threat-intel
```

### 2. Install Dependencies
#### Python Requirements
```sh
pip install flask paramiko mysql-connector-python requests
```

#### Database Setup (MySQL Example)
```sh
CREATE DATABASE honeypot_db;
USE honeypot_db;
CREATE TABLE attacks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip VARCHAR(255),
    payload TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Run the Honeypot
```sh
python honeypot.py
```

### 4. Start the Web Dashboard
```sh
python app.py
```

### 5. View Dashboard
Open your browser and go to:
```
http://localhost:5000
```

## Sample Code
### Fake SSH Honeypot
```python
import socket
import threading

def handle_client(client_socket):
    client_socket.send(b"Fake SSH Server. Enter Password: ")
    response = client_socket.recv(1024)
    print(f"[*] Attack attempt from {client_socket.getpeername()} with password: {response.decode().strip()}")
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 2222))
server.listen(5)
print("[*] Honeypot listening on port 2222")

while True:
    client, addr = server.accept()
    print(f"[*] Connection from {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
```

## Future Enhancements
- Machine learning-based anomaly detection
- Integration with SIEM tools (Splunk, ELK Stack)
- Dynamic firewall blocking based on attack trends

## License
This project is open-source under the MIT License.

## Author
**Your Name** - [GitHub Profile](https://github.com/yourusername)
