from flask import Flask,request
 

app=Flask(__name__)

@app.route('/')
def handle_home():
    return 'OK',200

app.route('/twilio',methods=['POST'])
def handle_twilio():
    body=request.form.to_dict()
    print(body)
    return 'OK',200
