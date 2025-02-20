from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    ip = request.headers.get("Cf-Connecting-Ip")
    print(request.headers)

    return render_template("index.html",ip=ip)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=20010, debug=True)
