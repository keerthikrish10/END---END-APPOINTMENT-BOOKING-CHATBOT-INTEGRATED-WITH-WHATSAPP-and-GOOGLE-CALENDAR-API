import sqlite3

def create_patient_table():
    """ Create a table to store patient details if it doesn't exist """
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  email TEXT,
                  age INTEGER,
                  gender TEXT,
                  doctor_type TEXT,
                  location TEXT,
                  start_time TEXT,
                  end_time TEXT)''')
    conn.commit()
    conn.close()
    print('success')

def insert_patient_details(patient_details):
    """ Insert patient details into the database """
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute('''INSERT INTO patients (name, email, age, gender, doctor_type, location, start_time, end_time)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
              (patient_details['name'], patient_details['email'], patient_details['age'], patient_details['gender'],
               patient_details['doctor_type'], patient_details['location'], patient_details['start_time'], patient_details['end_time']))
    conn.commit()
    conn.close()

