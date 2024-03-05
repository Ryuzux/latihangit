from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {"username": "passwordd"}

@auth.verify_password
def verify_password(id, pas):
    user_password = users.get(id)
    if user_password and user_password == pas:
        return users

@app.route('/')
@auth.login_required
def home():
    return 'HOME'

@app.route('/equality')
def equality():
    return 'try method get, post, put, delete'

@app.route('/equality/get', methods=['GET'])
def get_equality():
    input_string = 'equality'
    dict_arr = {}
    max_num = 0
    for i in input_string:
        if i in dict_arr:
            dict_arr[i] += 1
        else:
            dict_arr[i] = 1
    for i, j in dict_arr.items():
        if j > max_num:
            max_num = j
    result = len(input_string) - max_num
    return jsonify({'result': result})

@app.route('/equality/post/<int:postEquality>', methods=['POST'])
def post_equality(postEquality):
    shared = 5
    cumulative = 0
    for i in range(postEquality):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return jsonify({'result': cumulative})

@app.route('/equality/put', methods=['PUTIN'])
def permutation_equation():
    putEquality = request.headers.get('putEquality')
    data = putEquality.split(',')
    data1 = list(map(int, data))
    result = []
    for i in range(1, len(data1)+1):
        index1 = data1.index(i) + 1
        index2 = data1.index(index1) + 1
        result.append(index2)
    return jsonify({'result':result})

@app.route('/equality/delete/<delete_resource>', methods=['DELETE'])
def delete_resource(delete_resource):
    return jsonify({'message': f'Deleted resource {delete_resource}'})

if __name__ == '__main__':
    app.debug = True
    app.run()
