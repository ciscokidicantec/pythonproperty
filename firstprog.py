from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='GET':
        # Handle POST Request here
        name = request.args.get("name")
        return render_template('index.html',name=name)
    return render_template('index.html',name="not a get")

if __name__ == '__main__':
    #DEBUG is SET to TR
    # UE. CHANGE FOR PROD
    app.run(port=5000,debug=True)

import helpers
from helpers import display

helpers.display("Another Message",True)
display("Sample Message")


myname = input("Enter Your Name")
print("Hello World")
print(myname)