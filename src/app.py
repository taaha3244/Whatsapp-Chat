from flask import Flask,request
 

app=Flask(__name__)

@app.route('/')
def handle_home():
    return 'OK',200

@app.route('/twilio',methods=['POST'])
def handle_twilio():
    data=request.form.to_dict()
    print(data['From'])
    print(data['Body'])
    return 'OK',200
