# WhatsApp-OpenAI Connection

This repository contains a demo project that connects Twilio and OpenAI to provide answers to user questions using OpenAI GPT-3. The project is written in Python and served with Flask. The chat-bot is capable of handling text messages and queries .

## Prerequisites

Before you start following this repository, make sure you have the following:

OpenAI API key: Create an account here and obtain the API key.
Twilio project: Get the Account SID and Auth Token for your Twilio project here.
API requesting application: Install a tool like Postman, Insomnia, etc.
NGROK for local testing.

## How to Use
To replicate the functionality of this repository and run it locally, follow these steps:

Create a .env file inside the root directory with the following environmental variables:

TWILIO_ACCOUNT_SID=YOUR_ACCOUNT_SID
TWILIO_AUTH_TOKEN=YOUR_AUTH_TOKEN
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
FROM=whatsapp:+14155238886
Note: The FROM variable in the .env file is the same for the Twilio WhatsApp Sandbox.

Create a virtual environment and activate it before installing the packages.

Install all the required dependencies from the requirements.txt file:


pip install -r requirements.txt
Run the server with either of the following commands:

python run.py
or
gunicorn run:app

Start NGROK engine on the same port as the Python application is running.

Provide the NGROK URL on Twilio WhatsApp Sandbox for all incoming requests.

Test the setup using your WhatsApp.

Feel free to explore and modify the code as needed for your own projects!
