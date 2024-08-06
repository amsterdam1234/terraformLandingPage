from flask import Flask , render_template, redirect
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
    return render_template('landingPage.html', hostname=hostname)

@app.route('/promethuse')
def promethuse():
    return redirect("http://prometheus.omer-amsterdam.com:9090")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)