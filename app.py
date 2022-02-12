from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/request', methods=["POST"])
def add_guide():
    title = request.json['title']
    content = request.json['content']
    return content

@app.route('/login',methods = ['POST'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="Ryan" and passwrd=="google1":  
          print(uname)
          return "Welcome %s" %uname 
          

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')