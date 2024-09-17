# END---END-APPOINTMENT-BOOKING-CHATBOT-INTEGRATED-WITH-WHATSAPP-and-GOOGLE-CALENDAR-API


Project Overview
This project is a Doctor Appointment Booking Chatbot built using Twilio's WhatsApp API, Flask, and Google Calendar API. The chatbot enables patients to schedule appointments with doctors through WhatsApp. It first collects the patient's preferred doctor type, location, and desired appointment date/time. If the selected time slot is unavailable, it retrieves available slots from the doctor's Google Calendar. After the appointment is booked, the chatbot gathers the patient's personal information (name, email, age, gender) and stores it in a database, along with the appointment details.

Key Features


WhatsApp Chatbot: Interact with patients over WhatsApp to schedule appointments.
Doctor Selection: Patients can specify the type of doctor they want to book.
Location and Time Input: The bot collects the location, date, and time preferences from the patient.
Google Calendar Integration: The chatbot checks the doctor’s availability and retrieves free time slots using Google Calendar API.
Appointment Confirmation: After scheduling, the chatbot gathers patient details (name, email, age, gender) and stores them in a database.
Twilio Integration: Twilio's WhatsApp API handles all message exchanges.
Flask Backend: The Flask application handles requests and interacts with Google Calendar, Twilio, and the database.
SQLite Database: Stores patient information and appointment details for further use.
Project Structure
bash
Copy code
doctor-appointment-bot/
│
├── app.py              # Main Flask application for handling WhatsApp requests and Google Calendar integration.
├── db_integration.py   # Contains functions to handle SQLite database operations.
├── requirements.txt    # Python package dependencies for the project.
├── .env                # Stores Twilio and Google API credentials securely.
├── templates/          # (Optional) HTML templates for any web-based interactions.
└── static/             # (Optional) Static files like images, CSS, and JavaScript.


Prerequisites:

Python 3.x
Twilio Account (for WhatsApp API)
Google Calendar API access
ngrok (optional, for local testing)
SQLite (or any other database)
Setup Instructions
Step 1: Clone the Repository
bash

cd doctor-appointment-bot
Step 2: Create a Virtual Environment
bash

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt
Step 4: Set Up Environment Variables
Create a .env file in the root directory with the following content:

bash
Copy code
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+your_twilio_whatsapp_number
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_CALENDAR_ID=doctor_calendar_id

Step 5: Set Up Google Calendar API
Follow Google Calendar API Documentation to enable the API and get your credentials.
Add your Google Calendar credentials in the .env file.

Step 6: Run the Flask App
bash
Copy code
python app.py

Step 7: Expose Your Local Server (for testing with Twilio)
To expose your Flask app to the internet for Twilio to communicate, use ngrok:

bash
Copy code
ngrok http 5000
Copy the public URL provided by ngrok and update it in the Twilio Console for the WhatsApp sandbox webhook URL.

Step 8: Test the Bot
Send "hello" to your Twilio WhatsApp number to initiate the conversation.
Follow the chatbot's prompts to book an appointment.
Usage
Send "hello" via WhatsApp to start interacting with the chatbot.
Follow the chatbot's guided steps to book an appointment, choose a doctor type, location, and appointment time.
If the requested time is unavailable, the bot will offer alternative time slots from Google Calendar.
After booking, provide your personal details (name, email, age, gender) to complete the process.


Technologies Used:
Python: Backend logic with Flask.
Twilio: WhatsApp API for messaging.
Google Calendar API: To manage doctor availability.
Flask: Web framework for handling HTTP requests.
SQLite: For storing patient and appointment data.
