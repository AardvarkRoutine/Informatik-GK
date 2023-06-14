import sqlite3 as db
import os
import uuid
def add_patient(room, name, doctorid):
    # Adds a patient to the database 
    cur.execute('INSERT INTO patients (room, name, DoctorID) VALUES (?, ?, ?)', (room, name, doctorid))
    con.commit()

def add_doctor(name):
    # Adds a doctor to the database 
    cur.execute('INSERT INTO doctors (name) VALUES (?)', (doctorid, name))
    con.commit()

def add_nurse(nurseid, name):
    # Adds a nurse to the database 
    cur.execute('INSERT INTO nurses (nurseid, name) VALUES (?, ?)', (nurseid, name))
    con.commit()

def add_medicine(pzn, name, price):
    # Adds a medicine to the database 
    cur.execute('INSERT INTO medicines (pzn, name, price) VALUES (?, ?, ?)', (pzn, name, price))
    con.commit()

def add_patient_medicine(patientid, pzn):
    # Adds a medicine to a patient 
    cur.execute('INSERT INTO patient_medicine (patientid, pzn) VALUES (?, ?)', (patientid, pzn))
    con.commit()

def add_doctor_nurse(doctorid, nurseid):
    # Adds a nurse to a doctor 
    cur.execute('INSERT INTO doctor_nurse (doctorid, nurseid) VALUES (?, ?)', (doctorid, nurseid))
    con.commit()

def add_patient_file(patientid, filename):
    # Adds a file to a patient 
    cur.execute('INSERT INTO patient_files (patientid, filename) VALUES (?, ?)', (patientid, filename))
    con.commit()

con = db.connect('main.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS patients (patientid INTEGER PRIMARY KEY, room INTEGER, name TEXT, DoctorID INTEGER, FOREIGN KEY(DoctorID) REFERENCES doctors(doctorid))')
cur.execute('CREATE TABLE IF NOT EXISTS doctors (doctorid INTEGER PRIMARY KEY, name TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS nurses (nurseid INTEGER PRIMARY KEY, name TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS medicines (pzn INTEGER PRIMARY KEY, name TEXT, price INTEGER)')
cur.execute('CREATE TABLE IF NOT EXISTS patient_medicine (patientid INTEGER, pzn INTEGER, FOREIGN KEY(patientid) REFERENCES patients(patientid), FOREIGN KEY(pzn) REFERENCES medicines(pzn))')
cur.execute('CREATE TABLE IF NOT EXISTS doctor_nurse (doctorid INTEGER, nurseid INTEGER, FOREIGN KEY(doctorid) REFERENCES doctors(doctorid), FOREIGN KEY(nurseid) REFERENCES nurses(nurseid))')
cur.execute('CREATE TABLE IF NOT EXISTS patient_files (patientid INTEGER, filename TEXT, FOREIGN KEY(patientid) REFERENCES patients(patientid))')
con.commit()

"""The code above does the following:
1. Connects to the database
2. Creates a cursor for the database
3. Executes a SQL statement to create a table named patients (if it doesn't already exist) with the columns patientid, room, name and DoctorID
4. Executes a SQL statement to create a table named doctors (if it doesn't already exist) with the columns doctorid and name
5. Executes a SQL statement to create a table named nurses (if it doesn't already exist) with the columns nurseid and name
6. Executes a SQL statement to create a table named medicines (if it doesn't already exist) with the columns pzn, name and price
7. Executes a SQL statement to create a table named patient_medicine (if it doesn't already exist) with the columns patientid and pzn
8. Executes a SQL statement to create a table named doctor_nurse (if it doesn't already exist) with the columns doctorid and nurseid
9. Executes a SQL statement to create a table named patient_files (if it doesn't already exist) with the columns patientid and filename
10. Commits changes to the database"""

if os.path.isfile('setup.txt') == False:
    f = open('setup.txt', 'w')
    f.write('setup')
    f.close()
    patients_data = [
    (101, 'John Doe', 1),
    (102, 'Jane Smith', 2),
    (103, 'Bob Johnson', 2),
    (104, 'Alice Brown', 1),
    (105, 'David Lee', 3),
    (106, 'Emily Davis', 3),
    (107, 'Tom Wilson', 2)
    ]

    for patient in patients_data:
        add_patient(*patient)

    doctors_data = [
        (1, 'Dr. John Smith'),
        (2, 'Dr. Jane Brown'),
        (3, 'Dr. David Lee'),
        (4, 'Dr. Johnny Sins')
    ]

    for doctor in doctors_data:
        add_doctor(doctorid, doctor)

    nurses_data = [
    (1, 'Jane Doe'),
    (2, 'John Smith'),
    (3, 'Emily Jones'),
    (4, 'Michael Lee'),
    (5, 'Mary Jane')
    ]
    for nurse in nurses_data:
        add_nurse(nurse)

    medicines_data = [
        (123456, 'Paracetamol', 5),
        (234567, 'Ibuprofen', 10),
        (345678, 'Aspirin', 15),
        (456789, 'Morphine', 20),
        (567890, 'Codeine', 25),
        (678901, 'Oxycodone', 30),
        (789012, 'Hydrocodone', 35),
        (890123, 'Tramadol', 40),
        (901234, 'Diclofenac', 45),
        (912345, 'Naproxen', 50),
        (923456, 'Ketorolac', 55),
        (934567, 'Fentanyl', 60)
    ]

    for medicine in medicines_data:
        add_medicine(*medicine)

    patient_medicine_data = [
        (101, 123456),
        (101, 234567),
        (102, 345678),
        (102, 456789),
        (103, 567890),
        (103, 678901),
        (104, 789012),
        (104, 890123),
        (105, 123456),
        (105, 234567),
        (106, 345678),
        (106, 456789),
        (107, 567890),
        (107, 678901),
    ]

    for patient in patients_data:
        for medicine in medicines_data:
            cur.execute('INSERT INTO patient_medicine (patientid, pzn) VALUES (?, ?)', (patient[0], medicine[0]))
    con.commit()

    doctor_nurse_data = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (3, 1),
        (4, 2),
        (4, 3),
    ]

    for doctor_nurse in doctor_nurse_data:
        add_doctor_nurse(*doctor_nurse)

    for patient in patients_data:
        patient_id = patient[0]
        patient_name = patient[1]
        filename = str(uuid.uuid4())
        add_patient_file(patient_id, filename)

        # Write patient data to file
        with open(f'{filename}.txt', 'w') as f:
            f.write(f'Patient ID: {patient_id}\n')
            f.write(f'Patient Name: {patient_name}\n')
            f.write(f'File Name: {filename}\n')

    """ Here is the explanation for the code above:
    1. The code above checks for the existence of a file named setup.txt in the current directory. If the file doesn’t exist, it creates the file and writes the word setup to it. Then it proceeds to create the tables and populate them with data. 
    2. The code creates a list of tuples containing patient data. Each tuple contains three values: patient id (integer), patient name (string), and doctor id (integer). 
    3. The code then inserts the data into the patients table using the add_patient() function. The add_patient() function is defined below: """


# print the entire database
def print_database(table):
    print(table)
    cur.execute(f'SELECT * FROM {table}')
    print(cur.fetchall(),"\n")

tables = ['patients', 'doctors', 'nurses', 'medicines', 'patient_medicine', 'doctor_nurse', 'patient_files']
for table in tables:
    print_database(table)

""" Here is the explanation for the code above:
1. We use the execute function to execute the SQL query.
2. We use the fetchall function to fetch all of the results from the query.
3. We use the commit function to commit the changes to the database.
4. We use the close function to close the connection to the database. """

def custom_queries():
    # 1. get all patients with a certain doctor
    print("\033[1;31;40m patients with a certain doctor: \n")
    cur.execute('SELECT * FROM patients WHERE doctorid = 1')
    print(cur.fetchall())

    # 2. get which nurse treats which patient
    cur.execute('SELECT doctors.name AS doctor_name, nurses.name AS nurse_name FROM doctor_nurse JOIN doctors ON doctor_nurse.doctorid = doctors.doctorid JOIN nurses ON doctor_nurse.nurseid = nurses.nurseid')
    print(cur.description)
    print(cur.fetchall())

    # 3. get all patients with a certain medicine
    print("\033[1;31;40m patients with a certain medicine: \n")
    cur.execute('SELECT * FROM patients WHERE patientid = 1')
    print(cur.fetchall())

    # 4. get all doctors with a certain nurse
    print("\033[1;31;40m doctors with a certain nurse: \n")
    cur.execute('SELECT * FROM doctor_nurse WHERE nurseid = 1')
    print(cur.fetchall())

    # 5. Get all medicines with a certain patient
    print("\033[1;31;40m medicines with a certain patient: \n")
    cur.execute('SELECT * FROM patient_medicine WHERE patientid = 1')
    print(cur.fetchall())

print("\n\n")
custom_queries()