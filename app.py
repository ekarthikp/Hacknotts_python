from flask import Flask, request, jsonify
import base64
import os
from twilio.rest import Client
from twilio.rest import TwilioRestClient
from datetime import datetime
from datetime import datetime, timedelta



app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'  

@app.route('/request', methods=["POST"])
def add_guide():
    #title = request.json['title']
    if("content" in request.json):
         content = request.json['content']
    print(request.json)
    url=request.json['url']
    url=base64.b64decode(url).decode("utf-8")
    print(url)
    if "youtube" in url:
        msg= "Watching Youtube :" + url
        send_text(msg)
    return ""

@app.route('/login',methods = ['POST'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="Ryan" and passwrd=="google1":  
          print(uname)
          return "Welcome %s" %uname 

def send_text(msg):
    print(msg)
    account_sid = 'ACec171a119c791c205c71a012fa72e967' 
    auth_token = '7dbf2422fefa68ff24395411868c720d' 
    client = Client(account_sid, auth_token) 

    message = client.messages.create(
                              messaging_service_sid='MG16ab7d1555d148d28d80fbff12722672', 
                              body=msg,
                              to='+447879907243' ,
                              #send_at=send_when.isoformat() + 'Z',
                                #schedule_type='fixed'
                          )
    print(message.sid)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')