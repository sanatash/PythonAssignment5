from flask import Flask, request
import pymysql
import requests
import json

app = Flask(__name__)

@app.route('/dogs')
def get_dogs_data():
    #return "Hello!"
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='JLHNSONLhK', passwd='HE6DJPd5an', db='JLHNSONLhK')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("SELECT * from JLHNSONLhK.dogs")
    dog_list = {}
    dog_count = 1
    for row in cursor:
        dog_list[dog_count] = {'name': row[0], 'age': row[1], 'breed': row[2]}
        #dog_list[dog_count] = row
        dog_count+=1
        #yield row
    cursor.close()
    conn.close()
    return {'dogs': dog_list}

@app.route('/add_dog', methods=['GET', 'POST'])
def add_dog():
    #type = request.headers.get('Content-Type')
    #data = json.loads(request.data)
    request_data = request.get_json(force=True)
    request_data = request.json
    name = request_data.get('name')
    age = request_data.get('age')
    breed = request_data.get('breed')

    print(request_data)
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='JLHNSONLhK', passwd='HE6DJPd5an', db='JLHNSONLhK')
    conn.autocommit(True)
    cursor = conn.cursor()
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Breed: {breed}")

    cursor.execute(f"INSERT into JLHNSONLhK.dogs (name, age, breed) VALUES ('{name}', {age}, '{breed}')")
    cursor.close()
    conn.close()
    return request_data

app.run(host='127.0.0.1', debug=True, port=5000)

#res = requests.post('127.0.0.1:5000/add_dog', json={'name': 'sheleg', 'age':12, 'breed': 'husky'})