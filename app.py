import os
from flask import Flask, request, make_response
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Ensure Twilio credentials are loaded properly
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
    raise ValueError("Twilio Account SID and Auth Token must be set in environment variables")

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    # Get incoming message
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()
    
    doctor_list = ['Cardiologist', 'Dermatologist', 'Pediatrician', 'Orthopedic', 'Ophthalmologist']
    doctor_str = "\n".join(doctor_list)  # Convert the list into a string format

    # Logic to respond to incoming messages
    if 'hello' in incoming_msg:
        msg.body(f'Hello! Please select your preferred type of doctor from the following list:\n{doctor_str}')
    elif incoming_msg.capitalize() in doctor_list:
        msg.body('Please provide your location and preferred date and time for the appointment.')
    else:
        msg.body('I am sorry, I didn’t understand that. Can you please try again?')

    # Set Content-Type to XML
    resp = make_response(str(response))
    resp.headers['Content-Type'] = 'application/xml'
    return resp

if __name__ == '__main__':
    app.run(port=5000, debug=True)
