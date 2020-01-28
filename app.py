from flask import Flask, render_template
import cx_Oracle
import sys
import os

# declare constants for flask app
HOST = '0.0.0.0'
PORT = 5000

# initialize flask application
app = Flask(__name__)

# db connection constants
# update below with your db credentials
DB_IP = os.getenv('DB_IP')
SID = "aTFdb"
DB_PORT = 1521
DB_USER = "dbfirst"
DB_PASSWORD = "DevOps_123#"

# make dsn and create connection to db
dsn_tns = cx_Oracle.makedsn(DB_IP, DB_PORT, SID)
connection = cx_Oracle.connect(DB_USER, DB_PASSWORD, dsn_tns)


# sample api endpoint returning data from db

@app.route('/api')
def test():
    data = ''
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM dept"):
        print (row)
        data = data + str(row)
    cursor.close()
    data = data[2:len(data)-3]
    final_result = str(data)
    return render_template('index.html', db_data=final_result)

# main

if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
