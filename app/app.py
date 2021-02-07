from flask import Flask, request, jsonify, Response
import json
import mysql.connector


app = Flask(__name__)

config = {
    'user': 'root',
    'host': 'mysql',
    'database': 'odwta'
    }



@app.route('/person', methods=['POST'])
def postPerson():

        connection = mysql.connector.connect(**config)
        
        mycursor = connection.cursor()

        sql = "INSERT INTO persons (Firstname, Lastname) VALUES (%s, %s)";
        val = (request.form['firstname'], request.form['lastname'])
        #val = (request.form.get('firstname'), request.form.get('lastname'))
        #val = ("John", "Highway")
        mycursor.execute(sql, val);
        #mycursor.execute(sql)

        print(mycursor.rowcount, "record inserted.")

        connection.commit()
        mycursor.close()
       
        return Response(status=200)

@app.route('/persons', methods=['GET', 'POST'])
def home():
        connection = mysql.connector.connect(**config)
        
        mycursor = connection.cursor()

        mycursor.execute("SELECT * FROM persons")

        myresult = mycursor.fetchall()

        persons = []
        for row in myresult:
            persons.append({'PersonID': row[0], 'Firstname': row[1], 'Lastname':row[2]})
        return json.dumps(persons) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

