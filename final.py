#cecking github

#import json
import decimal
from decimal import Decimal



import logging

import simplejson as json

from flask import Flask,redirect,url_for,render_template,request, jsonify
import mysql.connector.connection

from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.types import Integer
#from sqlalchemy.types import NULLTYPE


import os
from werkzeug.utils import secure_filename

from PIL import ImageTk,Image
#from PIL.Image import core as _imaging

#from tkinter import *
import tkinter as tk
from tkinter import Menu,Label,Button
from tkinter import mainloop
#from tkinter import Tk

from tkinter.filedialog import askopenfilename


#need pip install flask-nav
#from flask_nav import Nav
#from flask_sqlalchemy import SQLAlchemy



#from flask_wtf import FlaskForm
from flask import Flask,redirect,url_for,render_template,request

#app=Flask(__name__)

#from mariopropertyenv.databaseexists import databaseexists
#from databaseexists import databaseexists,checkdatabaseexists,checktableexists,testfunc

from databaseexists import checkdatabaseexists,testfunc
import databaseexists

app=Flask(__name__)
#nav = Nav(app)

#app.config['SQLACHEMY_DATABASE_URI'] = 'mysql://root:Coreldraw1$@localhost/mymariodatabase'
#app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

#logging.basicConfig(filename="c:\\compress\\errorlogger\\python.log", level=logging.DEBUG)
#logger = logging.getLogger()


#db = SQLAlchemy(app)

#class customers(db.Model):
 # sqlachemyid = db.Column(db.Integer, primary_key=True)
  #sqlachemyname = db.Column(db.String(80),unique=True)
  #sqlachemyvendorname = db.Column(db.String(80),unique=True)
#=======================================================================================================================
@app.route('/',methods=['GET','POST'])
def j():

    try:

        mydb = mysql.connector.connect(host="localhost",auth_plugin='mysql_native_password',user="root",password="Coreldraw1$")
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS mymariodatabase")

        mydbtb = mysql.connector.connect(host="localhost",auth_plugin='mysql_native_password',user="root",password="Coreldraw1$",database="mymariodatabase")
        mycursor1 = mydbtb.cursor()

        dropsqlcustomersjoin = "DROP TABLE IF EXISTS customersjoin"
        mycursor1.execute(dropsqlcustomersjoin)
        #mydbtb.commit()
        dropsqlimagesjoin = "DROP TABLE IF EXISTS imagesjoin"
        mycursor1.execute(dropsqlimagesjoin)



        mycursor1.execute("CREATE TABLE customersjoin (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), price Decimal(10,0), estatedes VARCHAR(1000), fulldes LONGTEXT, onmarketdate VARCHAR(45))")

        sql = "INSERT INTO customersjoin (name, address, price, estatedes, fulldes, onmarketdate) VALUES (%s, %s, %s, %s, %s,%s)"
        val = [
            ('Peter', 'Lowstreet 4',148000,"This is 200 metres from the sea","Opening Hours",'2012-01-01'),
            ('Amy', 'Apple st 652',74000,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Hannah', 'Mountain 21',675000,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Michael', 'Valley 345',98000,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Sandy', 'Ocean blvd 2',187000,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Betty', 'Green Grass 1',133000,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Richard', 'Sky st 331',998000,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Susan', 'One way 98',12670567,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Vicky', 'Yellow Garden 2',556000,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Ben', 'Park Lane 38',78000,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('William', 'Central st 954',245000,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Chuck', 'Main Road 989',67800,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Viola', 'Sideway 1633',55123,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Jade', 'West Swindon',67890,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012'),
            ('Helen', 'Stratton St. Margaret',23555,"Quality doesnt have to be complicated. Sometimes","Closing Times",'1-01-2012')
          ]

        mycursor1.executemany(sql, val)
        mycursor1.close()

        mydbtb.commit()

        mydbtbjoin = mysql.connector.connect(host="localhost",auth_plugin='mysql_native_password',user="root",password="Coreldraw1$",database="mymariodatabase")
        mycursorjoin = mydbtbjoin.cursor()
        mycursorjoin.execute("CREATE TABLE imagesjoin(idmyimages INT PRIMARY KEY, estatelink INT, imagepath VARCHAR(255))")

        sqlimage = "INSERT INTO imagesjoin (idmyimages, estatelink, imagepath) VALUES (%s, %s, %s)"
        valimage = [(1,	1, "/static/uploadimages/IMG_20190429_155354_6.jpg"),
	                (2,	3, "/static/uploadimages/IMG_20190821_153148_5.jpg"),
	                (3,	4, "/static/uploadimages/IMG_20190808_125728_5.jpg"),
	                (4,	4,"/static/uploadimages/IMG_20190429_155354_6.jpg"),
	                (5,	4, "/static/uploadimages/IMG_20190821_153148_5.jpg"),
	                (6,	4, "/static/uploadimages/IMG_20190808_125728_33.jpg"),
	                (7,	2, "/static/uploadimages/IMG_20190808_125724_1.jpg"),
	                (8,	2, "/static/uploadimages/IMG_20190808_125717_5.jpg"),
	                (9,	3, "/static/uploadimages/IMG_20190808_125618_1.jpg"),
	                (10, 6, "/static/uploadimages/IMG_20190808_125614_3.jpg"),
	                (11, 4,	"/static/uploadimages/IMG_20190808_125543_6.jpg"),
	                (12, 5,	"/static/uploadimages/IMG_20190429_182340_7.jpg"),
	                (13, 14, "/static/uploadimages/IMG_20190429_182315_5.jpg"),
	                (14, 2,	"/static/uploadimages/IMG_20190429_181711_3.jpg"),
	                (15, 7,	"/static/uploadimages/IMG_20190429_181642_7.jpg"),
	                (16, 1,	"/static/uploadimages/IMG_20190429_181624_2.jpg"),
	                (17, 3,	"/static/uploadimages/IMG_20190429_181624_2.jpg"),
	                (18, 15, "/static/uploadimages/helen.jpg"),
	                (19, 8,	"/static/uploadimages/helen.jpg"),
	                (20, 9,	"/static/uploadimages/helen.jpg")]

        mycursorjoin.executemany(sqlimage, valimage)
        mydbtbjoin.commit()
     #   mydbtb.close()

        mydbtbselectconn = mysql.connector.connect(host="localhost",auth_plugin='mysql_native_password',user="root",password="Coreldraw1$",database="mymariodatabase")
        #mycursor = mydbtbselectconn.cursor()
        mycursor = mydbtbselectconn.cursor(dictionary=True)
        #    sql_select_Query = mycursor.execute("SELECT * FROM customers")
        #sql_select_Query = mycursor.execute("SELECT name, address, picturpath, idforeign, price FROM customers")

        #sql_select_Query = mycursor.execute("SELECT name, address, picturpath, price FROM customersjoin WHERE customersjoin.id > 0")

        sql_select_Query = """SELECT count(imagesjoin.estatelink) as lcount,customersjoin.id, customersjoin.name, customersjoin.address,price,imagesjoin.imagepath
                            FROM customersjoin
                            INNER JOIN imagesjoin
                            ON customersjoin.id = imagesjoin.estatelink
                            GROUP BY customersjoin.name,imagesjoin.imagepath
                            ORDER BY customersjoin.id DESC;"""

        mycursor.execute(sql_select_Query)
        rowreturn = mycursor.fetchall()
    except:
        print("Something Went Wrong")
    finally:
        print("hit finally try block - all good")
        #mycursor.close


    #jsontuplelist = json.dumps(decimal.Decimal('2.2'))

    #jsontuplelist = json.dumps(rowreturn, tuple_as_array=True)


    jsontuplelist = json.dumps(rowreturn)

    #this save the json in a file so needs fp:
    #nonstring = json.dump(rowreturn)


   # r = json.dumps(jsontuplelist)

    print(jsontuplelist)

    return render_template('testdebug.html', stud_json=jsontuplelist)
    #return render_template('joinedimages.html', stud_json=jsontuplelist)
    #return render_template('joinedimages.html')    


#=========================================================================================================================

@app.route('/j',methods=['GET','POST'])
def s():

    conn = mysql.connector.connect(host="localhost",user="root",password="Coreldraw1$",database="mymariodatabase")
    cursor = conn.cursor()

    if conn:
        print ("Connected Successfully")
    else:
        print ("Connection Not Established")

    thisdict = {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964
    }  

    print(thisdict["model"])
    print(thisdict["year"])      
      

    class create_dict(dict): 
  
        # __init__ function 
        def __init__(self): 
            self = dict() 
          
        # Function to add key:value 
        def add(self, key, value): 
            self[key] = value

    mydict = create_dict()

    #select_customers = """SELECT name, address, picturpath, price, idforeign FROM customers"""
    
    select_customers = """SELECT name, address, picturpath, price, estatedes, fulldes, onmarketdate FROM customers"""

    
    
    cursor.execute(select_customers)
    result = cursor.fetchall()

    #jsonf = jsonify(result)

    #print(jsonf)

    for row in result:
       # mydict.add(row[0],({"name":row[1],"address":row[2],"picturpath":row[3],"price":row[4],"idforeign":row[5]}))
       # mydict.add(row[0],({"address":row[1],"picturpath":row[2],"price":row[3], "idforeign":row[4]}))
        mydict.add(row[0],({"address":row[1],"picturpath":row[2],"price":row[3], "estatedes":row[4], "fulldes":row[5], "onmarketdate":row[6]}))

    print(mydict)

    stud_json = json.dumps(mydict, indent=2)
 #   stud_json = json.dumps(mydict, indent=2, sort_keys=True)

 # create a simple JSON array
 #   jsonString = '{"key1":"value1","key2":"value2","key3":"value3"}'

    # change the JSON string into a JSON object
    jsonObject = json.loads(stud_json)

 #   for key in jsonObject:
 #       for details in key:
 #           print("Here Should Be My Address = ",details)

    #replace ' with "" string.replace(old, new, count)

    # print the keys and values
    for key in jsonObject:
        value = jsonObject[key]
 #       value = value.replace("'",'"')
        myadd = value['address']
        print("\nThe Address = ",myadd)
        mypictpath = value['picturpath']
        print("The Picture Path = ",mypictpath)
        myprice = value['price']
        print("The Price = £{}".format(myprice))
    #    myforeign = value['idforeign']
    #    print("The Foreign Key Value = ",myforeign)

    return render_template('joined.html', stud_json=stud_json)    

#=========================================================================================================================


@app.route('/s',methods=['GET','POST'])
def home():

    def NewFile():
        print("New File!")
    def OpenFile():
        name = askopenfilename()
        print(name)
    def About():
        print("This is a simple example of a menu")
    
    root = tk.Tk()
    root.title("TESTING MAKING GUI USING tkinter")
    root.iconbitmap("C:\\pythoncode\\bing.ico")
    #canvas = tk.Canvas(root, height='200', width = '300')
    #canvas.pack()
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open...", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)

    my_img1 = ImageTk.PhotoImage(Image.open("C:\\pythoncode\\static\\helen.jpg"))
    my_img2 = ImageTk.PhotoImage(Image.open("C:\\pythoncode\\static\\uploadimages\\IMG_20190429_155507_3.jpg"))
    my_img3 = ImageTk.PhotoImage(Image.open("C:\\pythoncode\\static\\uploadimages\\IMG_20190429_155349_4.jpg"))
    my_img4 = ImageTk.PhotoImage(Image.open("C:\\pythoncode\\static\\helen.jpg"))
    my_img5 = ImageTk.PhotoImage(Image.open("C:\\pythoncode\\static\\helen.jpg"))
    my_img6 = ImageTk.PhotoImage(Image.open("C:\\pythoncode\\static\\helen.jpg"))
    my_img6 = ImageTk.PhotoImage(Image.open("C:\\pythoncode\\static\\helen.jpg"))

    image_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]

    #my_img = ImageTk.PhotoImage(Image.open("C:\\pythoncode\\static\\uploadimages\\IMG_20190429_174706_3.jpg"))

    my_label = Label(image=my_img1)
    #my_label.pack()
    my_label.grid(row=0, column=0, columnspan=3)

    def forward(image_number):
        global my_label
        global button_forward
        global button_back
        
        my_label.grid_forget()
        my_label = Label(image=image_list[image_number-1])
        button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
        button_back = Button(root, text="<<", command=lambda: back(image_number-1))

        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)

    def back(image_number):
        global my_label
        global button_forward
        global button_back

        my_label = Label(image=image_list[image_number-1])
        my_label.grid_forget()

        button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
        button_back = Button(root, text="<<", command=lambda: back(image_number-1))
        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)

    button_back = Button(root, text="<<", command= back)
    button_back.grid(row=1, column=0)
    button_exit = Button(root, text= "Exit Program", command= root.quit)
    button_exit.grid(row=1, column=1)
    button_forward = Button(root, text=">>", command=lambda: forward(2))
    button_forward.grid(row=1, column=2)


    root.mainloop()


    dmy = databaseexists.testfunc()
    print(dmy)
    #vc = databaseexists.checkdatabaseexists()



    databaseexists.databaseexists()
    databaseexists.checkdatabaseexists()
    databaseexists.checktableexists()
    if request.method=='POST':
        # Handle POST Request here
        mydb = mysql.connector.connect(host="localhost",user="root", password="Coreldraw1$", auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        sql = "DROP DATABASE IF EXISTS mymariodatabase"
        mycursor.execute(sql)
        mycursor.execute("CREATE DATABASE mymariodatabase")
        mydbtb = mysql.connector.connect(host="localhost",user="root",password="Coreldraw1$",database="mymariodatabase")
        mycursor1 = mydbtb.cursor()
        mycursor1.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), picturpath VARCHAR(255), price Decimal(10,0))")
        return render_template('showpicturers.html')
    
    mydb = mysql.connector.connect(host="localhost",user="root", password="Coreldraw1$", auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    sql = "DROP DATABASE IF EXISTS mymariodatabase"
    mycursor.execute(sql)
    mycursor.execute("CREATE DATABASE mymariodatabase")
    mycursor.close()
    
    try:

        mydbtb = mysql.connector.connect(host="localhost",user="root",password="Coreldraw1$",database="mymariodatabase")
        mycursor1 = mydbtb.cursor()
        mycursor1.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), picturpath VARCHAR(255), price Decimal(10,0), idforeign INT)")

        sql = "INSERT INTO customers (name, address, picturpath, price, idforeign) VALUES (%s, %s, %s, %s, %s)"
        val = [
            ('Peter', 'Lowstreet 4','/static/uploadimages/IMG_20190429_155354_6.jpg',148000,1),
            ('Amy', 'Apple st 652','/static/uploadimages/IMG_20190821_153148_5.jpg',74000,1),
            ('Hannah', 'Mountain 21','/static/uploadimages/IMG_20190808_125728_5.jpg',675000,3),
            ('Michael', 'Valley 345','/static/uploadimages/IMG_20190808_125724_1.jpg',98000,3),
            ('Sandy', 'Ocean blvd 2','/static/uploadimages/IMG_20190808_125717_5.jpg',187000,1),
            ('Betty', 'Green Grass 1','/static/uploadimages/IMG_20190808_125618_1.jpg',133000,1),
            ('Richard', 'Sky st 331','/static/uploadimages/IMG_20190808_125614_3.jpg',998000,1),
            ('Susan', 'One way 98','/static/uploadimages/IMG_20190808_125543_6.jpg',12670567,1),
            ('Vicky', 'Yellow Garden 2','/static/uploadimages/IMG_20190429_182340_7.jpg',556000,1),
            ('Ben', 'Park Lane 38','/static/uploadimages/IMG_20190429_182315_5.jpg',78000,3),
            ('William', 'Central st 954','/static/uploadimages/IMG_20190429_181711_3.jpg',245000,3),
            ('Chuck', 'Main Road 989','/static/uploadimages/IMG_20190429_181642_7.jpg',67800,1),
            ('Viola', 'Sideway 1633','/static/uploadimages/IMG_20190429_181624_2.jpg',55123,2),
            ('Jade', 'West Swindon','/static/uploadimages/IMG_20190429_181624_2.jpg',67890,1),
            ('Helen', 'Stratton St. Margaret','/static/uploadimages/helen.jpg',23555,1)
          ]

#/static/uploadimages/IMG_20190429_181610_6.jpg
#/static/uploadimages/IMG_20190429_174744_5.jpg
#/static/uploadimages/IMG_20190429_174719_3.jpg
#/static/uploadimages/IMG_20190429_174706_3.jpg
#/static/uploadimages/IMG_20190429_174700_2.jpg
#/static/uploadimages/IMG_20190429_174645_1.jpg
#/static/uploadimages/IMG_20190429_174504_3.jpg
#/static/uploadimages/IMG_20190429_174430_9.jpg
#/static/uploadimages/IMG_20190429_174410_6.jpg
#/static/uploadimages/IMG_20190429_174335_6.jpg
#/static/uploadimages/IMG_20190429_155507_3.jpg
#/static/uploadimages/IMG_20190429_155446_4.jpg
#/static/uploadimages/IMG_20190429_155354_6.jpg
#/static/uploadimages/IMG_20190429_155349_4.jpg
#/static/uploadimages/IMG_20190429_155345_9.jpg
					

        mycursor1.executemany(sql, val)
        mycursor1.close()

        mydbtb.commit()
        mydbtb.close()

        mydbtbselectconn = mysql.connector.connect(host="localhost",user="root",password="Coreldraw1$",database="mymariodatabase")
        mycursor = mydbtbselectconn.cursor()
        #    sql_select_Query = mycursor.execute("SELECT * FROM customers")
        #sql_select_Query = mycursor.execute("SELECT name, address, picturpath, idforeign, price FROM customers")

        sql_select_Query = mycursor.execute("SELECT name, address, picturpath, idforeign, price FROM customers WHERE customers.id < 3")

        mycursor.execute(sql_select_Query)
        rowreturn = mycursor.fetchall()

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
        #logger.error(e)
    else:
        print("else try block error")
    finally:
        print("hit finally try block")
        mycursor.close


    #jsontuplelist = json.dumps(decimal.Decimal('2.2'))

    #jsontuplelist = json.dumps(rowreturn, tuple_as_array=True)


    jsontuplelist = json.dumps(rowreturn)
   # r = json.dumps(jsontuplelist)

  #  print(jsontuplelist)



  #  return render_template('index.html',jsontuplelist = json.dumps(rowreturn))
    return render_template('index.html',rowreturn=rowreturn, jsontuplelist=jsontuplelist)
    #return render_template('index.html',rowreturn=rowreturn, jsontuplelist=jsontuplelist, context={'rowreturn': rowreturn})
    
    #return render_template('index.html',rowreturn=rowreturn)

#app.config["image_uploads"] = 'C:\pythoncode\static'
#app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPG","GIF","JPEG","GIF"]


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = r'\static\uploadimages'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
MAX_FILE_SIZE = 16
#MAX_FILE_SIZE = 16 * 1024 * 1024
app.config['MAX_CONTENT_PATH'] = MAX_FILE_SIZE

@app.route('/',methods=['GET','POST'])
def home1():
    return 'hell'

@app.route('/upload_image',methods=['GET','POST'])
def upload_image():

    mycwd = os.getcwd()
    print(mycwd)

    if request.method == "POST":

        if request.files:

           # myimage = request.files["inpFile[]"]
            #for allpics in myimage:
              #  print(allpics) 

            list=[] #myfile is the key of a multi value dictionary, values are the uploaded files
            for f in request.files.getlist("inpFile[]"): #myfile is the name of your html file button
                filename = f.filename
                #filename = f
                list.append(filename)

                if filename == "":
                    print("File Has No Name")
                    return redirect(request.url)

                myfilename = secure_filename(filename)

                mydownloadpath = mycwd + os.path.join(app.config['UPLOAD_FOLDER'], myfilename)


                f.save(mydownloadpath)

            #myimage.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

           # myimage.save(myimage.filename)
            return redirect('/upimg')

    return render_template('previewpicture.html')

@app.route('/upimg',methods=['GET'])
def upimg():
    return render_template('previewpicture.html')    


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5500,debug=True)
