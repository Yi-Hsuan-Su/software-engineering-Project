from flask import Flask , jsonify , request
from mongoengine import *
import json
from bson import ObjectId
from flask_cors import cross_origin

app = Flask(__name__)

app.config["MONGODB_DB"] = 'KEELUNG_EAT'
connect(
    host='mongodb+srv://EthanSu:Eason861208@cluster0-upq73.gcp.mongodb.net/KEELUNG_EAT?retryWrites=true&w=majority',
    port=27017
)

class User(Document):
  name = StringField(required=True)
  email =  StringField()
  password = StringField()
  district = StringField()
  address = StringField()
  identity = StringField()
  status = StringField()
  tel = StringField()
  meta = {'collection': 'User'}
#----------------------------------------------------------
@app.route('/User/View_Delivery' , methods = ['GET']) 
@cross_origin()
def view_all_delievery_man ():
 Users =  User.objects().all()
 output = []
 for user in Users:
      if user['identity'] is '1' :
       output.append( {'id': str(user['id']) , 'name' : user['name'] , 'email' : user['email'] , 'password' : user['password'] , 'district' : user['district'] , 'address' : user['address'] , 'identity' : user['identity'] , 'status' : user['status'] , 'tel' : user['tel'] } )
    
 return jsonify(output)


@app.route('/User/View_User' , methods = ['GET']) 
@cross_origin()
def view_all_user ():
 Users =  User.objects().all()
 output = []
 for user in Users:
      if user['identity'] is '0' :
       output.append( {'id': str(user['id']) , 'name' : user['name'] , 'email' : user['email'] , 'password' : user['password'] , 'district' : user['district'] , 'address' : user['address'] , 'identity' : user['identity'] , 'status' : user['status'] , 'tel' : user['tel'] } )
    
 return jsonify(output)
 
 
@app.route('/User/View_User_and_Delivery' , methods = ['GET']) 
@cross_origin()
def view_all_user_delievery ():
 Users =  User.objects().all()
 output = []
 for user in Users:
       output.append( {'id': str(user['id']) , 'name' : user['name'] , 'email' : user['email'] , 'password' : user['password'] , 'district' : user['district'] , 'address' : user['address'] , 'identity' : user['identity'] , 'status' : user['status'] , 'tel' : user['tel'] } )
    
 return jsonify(output)
 


@app.route('/User/insert' , methods=['POST'] )
@cross_origin()
def create_delievery():

  data = request.json
  user = User(name = str(data['name']) , email = str(data['email']) , password = str(data['password']) , district = str(data['district']) , address = str(data['address']) , identity = '0' , status = '0' , tel = str(data['tel'])  )
  user.save()
  return jsonify(True)


@app.route('/User/delete' , methods=['POST'])
@cross_origin()
def delete_delievery():
  
  data = request.json
 # print(request.get_json()) 
  User.objects(id = str(data['id']) ).delete()
  return jsonify(True)



@app.route('/User/modify' , methods = ['POST'])
@cross_origin()
def modify_delievery():

  data = request.json
  
  User.objects(id = str(data['id'])).update( name = str(data['name'])) 
  if 'password' in data :
   User.objects(id = str(data['id'])).update( password = str( data['password'] ) ) 
  User.objects(id = str(data['id'])).update( district = str( data['district'] ) )
  User.objects(id = str(data['id'])).update( address = str (data['address'] ) )
  if 'identity' in data :
   User.objects(id = str(data['id'])).update( identity = str ( data['identity'] ) )
  User.objects(id = str(data['id'])).update( tel =  str(data['tel'] ) )  

  

  return jsonify(True)

if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')

