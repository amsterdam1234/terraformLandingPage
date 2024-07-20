from flask import Flask
import socket

###### App setup
app = Flask(__name__)


##session
app.secret_key = '123'
# Set up session defaults

#set up health check
@app.route('/health')
def health():
    return "OK", 200

@app.route('/')
def home():
    hostname = socket.gethostname()
    return "Hello, World! runing on host: " + hostname

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)