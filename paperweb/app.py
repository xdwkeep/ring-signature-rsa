from flask import Flask, request, render_template, jsonify
import json
from rsaInit import rsa_init
from rsaSigGen import sig_gen
from rsaVerifySig import sig_verify
from rsaVerifyRelevance import relevace_verify

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
    with open('db/n_all.json', 'r') as f:
        n = int(f.read())
    return render_template('index.html', n=n)


@app.route('/rsaInit.do', methods=['POST'])
def rsainit():
    data = request.get_data()
    json_data = json.loads(data)
    print(json_data)
    n = int(json_data['n'])
    rsa_init(n)
    return jsonify({"msg": 0, "data": "初始化完成"})


@app.route('/rsaSigGen.do', methods=['POST'])
def rsaSigGen():
    data = request.get_data()
    json_data = json.loads(data)
    print(json_data)
    k = int(json_data['k'])
    with open('db/n_all.json', 'r') as f:
        n_all = int(f.read())
    with open('db/message.txt', 'w') as f:
        f.write(json_data['ms'])
    with open('db/flagakr.json', 'w') as f:
        f.write(json_data['flagakr'])
    userstr = json_data['userstr']
    struserlist = userstr.split(',')
    userlist = [int(struser) for struser in struserlist]
    sig_gen(n_all, k, userlist)
    with open('db/sigma.txt', 'r') as f:
        sigma = f.read()
    return jsonify({"msg": 0, "data": sigma})


@app.route('/rsaVerifySig.do', methods=['POST'])
def rsaVerifySig():
    data = request.get_data()
    json_data = json.loads(data)
    print(json_data)
    with open('db/message.txt', 'w') as f:
        f.write(json_data['vsm'])
    with open('db/sigma.txt', 'w') as f:
        f.write(json_data['vssigma'])
    if sig_verify():
        return jsonify({"msg": 0, "data": "true"})
    else:
        return jsonify({"msg": 0, "data": "false"})


@app.route('/rsaVerifyRelevance.do', methods=['POST'])
def rsaVerifyRelevance():
    data = request.get_data()
    json_data = json.loads(data)
    print(json_data)
    with open('db/vr_sigma_u0.txt', 'w') as f:
        f.write(json_data['vrsigma1'])
    with open('db/vr_sigma_u1.txt', 'w') as f:
        f.write(json_data['vrsigma2'])
    if relevace_verify():
        return jsonify({"msg": 0, "data": "true"})
    else:
        return jsonify({"msg": 0, "data": "false"})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
