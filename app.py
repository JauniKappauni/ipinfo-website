from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    ipv4 = request.remote_addr

    return render_template("index.html",ipv4=ipv4)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=20010, debug=True)
