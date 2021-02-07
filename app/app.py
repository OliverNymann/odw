from flask import Flask, request, jsonify, Response
import json
import mysql.connector


app = Flask(__name__)

config = {
    'user': 'root',
    'password': '',
    'host': 'mysql',
    'port': '3307',
    'database': 'odwta'
    }


#def connectionToDB():
#    return connection
#def getDatabaseConnection():
#    return mysql.connector.connect(user="root", host="mysql", port="3307", password="", database="odwta")

@app.route('/person', methods=['GET', 'POST'])
def home():
        connection = mysql.connector.connect(**config)
        #sqlstr = "INSERT INTO persons(firstname, lastname) VALUES (%s %s)", (request.form.get('firstname'), request.form.get('lastname'))
        #cur = db.cursor()
        #cur.execute(sqlstr)
        #db.commit()
        mycursor = connection.cursor()

        mycursor.execute("SELECT * FROM persons")

        myresult = mycursor.fetchall()

        #return Response(status=200)
        return jsonify(myresult)
#mysql = MySQL(app)

#@app.route('/person', methods=['GET' , 'POST'])
#def home():
 #   if request.method == "POST":
  #      details = request.form
   #     firstname = details['firstname']
    #    lastname = details['lastname']
     #   cur = mysql.connection.cursor()
      #  cur.execute("INSERT INTO persons(Firstname, Lastname) VALUES (%s %s)", (firstname, lastname))
       # mysql.connection.commit()
        #cur.close()
        #return 'success'
    #return render_template('insert.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

