import subprocess
import tempfile
import os
from flask import Flask, render_template, redirect
import socket

hostname = socket.gethostname()

###### App setup
app = Flask(__name__)

##session
app.secret_key = '123'


# Set up session defaults

# set up health check
@app.route('/health')
def health():
    return "OK", 200


@app.route('/')
def home():
    return render_template('landingPage.html')


@app.route('/promethuse')
def promethuse():
    return redirect("http://prometheus.omer-amsterdam.com:9090")


@app.route('/stress')
def stress():
    command = """#!/bin/bash

     # Check if stress is installed
     if ! command -v stress &> /dev/null
     then
         echo "stress is not installed, installing now..."
         sudo yum install -y stress
     else
         echo "stress is already installed."
     fi

     # Activate stress
     echo "Activating stress..."
     stress --cpu 4 --timeout 600
     """

    # Write the command to a temporary file
    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        f.write(command)
        temp_file_name = f.name

    # Make the temporary file executable
    os.chmod(temp_file_name, os.stat(temp_file_name).st_mode | 0o111)

    # Execute the temporary file
    subprocess.Popen([temp_file_name], shell=True)

    return "Stress test started", 200

@app.route('/architecture')
def architecture():
    return render_template('architecture.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
