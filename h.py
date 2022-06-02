
#Trying to add files to github
#github should be working
#Use environment estate this can be activated by estate/scripts/activate using the terminl command
#line


import sys
import mysql.connector
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    mydb = mysql.connector.connect(host = "localhost", auth_plugin='mysql_native_password', user = "root", passwd = "Coreldraw1$")
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE IF EXISTS TESTPROPERTY;")
    mycursor.execute("CREATE DATABASE TESTPROPERTY")
    mydb.close()

    with open('static\downloadedimages\sunbathing.jpg','rb') as rf:
        with open('static\downloadedimages\sunbathing_copy.jpg','wb') as wf:
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)

    print(sys.path)
    return 'Hello world!'

if __name__ == "__main__":
    app.run(debug = True)