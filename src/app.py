from flask import Flask,request

from helper_functions.openai_api import model_completion
from helper_functions.Twilio_api import send_twilio_message
app=Flask(__name__)

@app.route('/')
def handle_home():
    return 'OK',200

@app.route('/twilio',methods=['POST'])
def handle_twilio():
    data=request.form.to_dict()

    sender_id=data['From']
    query=data['Body']

    response=model_completion(query)
    send_twilio_message(response,sender_id)


    return 'OK',200
