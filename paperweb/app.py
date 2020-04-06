from flask import Flask, request, render_template, jsonify
import json
from myrsa.rsaInit import rsa_init

app = Flask(__name__)


@app.route('/test')
def testhtml():
    return render_template('test.html')


@app.route("/test.do", methods=['POST'])
def test():
    data = request.get_data()
    json_data = json.loads(data)
    print(json_data)
    print(json_data['title'])
    return jsonify({"msg": 0, "data": "ok"})


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rsaInit.do', methods=['POST'])
def rsainit():
    data = request.get_data()
    json_data = json.loads(data)
    print(json_data)
    n = int(json_data['n'])
    print(n)
    rsa_init(n)
    return jsonify({"msg": 0, "data": "初始化完成"})




if __name__ == '__main__':
    app.run(debug=True)
