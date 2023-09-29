from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app, resources={r"/saving_data": {"origins": "http://127.0.0.1:5500"}})

def signin(name, password):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ronsia123", auth_plugin="mysql_native_password", database="eco")
    cur = mydb.cursor(buffered=True)
    cur.execute('SELECT * FROM ecousers WHERE username = %s AND password = %s', (name, password))
    L = cur.fetchone()
    if L is None:
        cur.execute('INSERT INTO ecousers (username, password) VALUES (%s, %s)', (name, password))
        mydb.commit()
        L=[name,password,0,0,0]
    else:
        print("name:", L[0])
        print("password:", L[1])
        print("nop:", L[2])
        print("tc:", L[3])
        print("pc:", L[4])
    return L

@app.route('/process_data', methods=['POST'])
def process_data():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('name')
        password = data.get('passw')

        A = list(signin(username, password))

        result = {
            'username': username,
            'password': password,
            'NOP': A[2],
            'TC': A[3],
            'PC': A[4],
        }

        response = jsonify(result)

     
        response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')

        return response

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
