from flask import Flask, request, render_template, jsonify
import json

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
    print('get-------------------------------')
    return jsonify({"msg": 0, "data": "ok"})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
