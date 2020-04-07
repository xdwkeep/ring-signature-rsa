from flask import Flask, request, render_template, jsonify
import json
from rsaInit import rsa_init
from rsaSigGen import sig_gen

app = Flask(__name__)


@app.route('/test')
def testhtml():
    return render_template('test.html')


@app.route('/test2')
def testhtml2():
    return render_template('test2.html')


@app.route("/test.do", methods=['POST'])
def test():
    data = request.get_data()
    json_data = json.loads(data)
    print(json_data)
    print(json_data['title'])
    return jsonify({"msg": 0, "data": "ok"})

@app.route('/index.html')
@app.route('/')
def index():
    with open('db/n.json', 'r') as f:
        n = int(f.read())
    return render_template('index.html', n=n)


@app.route('/rsaInit.do', methods=['POST'])
def rsainit():
    data = request.get_data()
    json_data = json.loads(data)
    print(json_data)
    n = int(json_data['n'])
    print(n)
    rsa_init(n)
    return jsonify({"msg": 0, "data": "初始化完成"})


@app.route('/rsaSigGen.do', methods=['POST'])
def rsaSigGen():
    data = request.get_data()
    json_data = json.loads(data)
    print(json_data)
    k = int(json_data['k'])
    with open('db/n.json', 'r') as f:
        n = int(f.read())
    sig_gen(n, k)
    with open('db/sigma.txt', 'r') as f:
        sigma = f.read()
    return jsonify({"msg": 0, "data": sigma})


if __name__ == '__main__':
    app.run(debug=True)
