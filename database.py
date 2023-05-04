import sqlite3 as db
import os
exists = os.path.isfile('setup.txt')
if not exists:
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

    # insert the data into the patients table
    for patient in patients_data:
        add_patient(*patient)

    doctors_data = [
        ('Dr. John Smith'),
        ('Dr. Jane Brown'),
        ('Dr. David Lee'),
        ('Dr. Emily Davis')
    ]

    # insert the data into the doctors table
    for doctor in doctors_data:
        add_doctor(doctor)

    add_nurse('Jane Doe')
    add_nurse('John Smith')
    add_nurse('Emily Jones')
    add_nurse('Michael Lee')
    add_nurse('Mary Jane')

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

    for patient_medicine in patient_medicine_data:
        add_patient_medicine(*patient_medicine)

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

    patient_files_data = [
        (101, 'patient101.txt'),
        (102, 'patient102.txt'),
        (103, 'patient103.txt'),
        (104, 'patient104.txt'),
        (105, 'patient105.txt'),
        (106, 'patient106.txt'),
        (107, 'patient107.txt'),
    ]

    for patient_file in patient_files_data:
        add_patient_file(*patient_file)


con = db.connect('database.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS patients (patientid INTEGER PRIMARY KEY, room INTEGER, name TEXT, DoctorID INTEGER, FOREIGN KEY(DoctorID) REFERENCES doctors(doctorid))')
cur.execute('CREATE TABLE IF NOT EXISTS doctors (doctorid INTEGER PRIMARY KEY, name TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS nurses (nurseid INTEGER PRIMARY KEY, name TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS medicines (pzn INTEGER PRIMARY KEY, name TEXT, price INTEGER)')
cur.execute('CREATE TABLE IF NOT EXISTS patient_medicine (patientid INTEGER, pzn INTEGER, FOREIGN KEY(patientid) REFERENCES patients(patientid), FOREIGN KEY(pzn) REFERENCES medicines(pzn))')
cur.execute('CREATE TABLE IF NOT EXISTS doctor_nurse (doctorid INTEGER, nurseid INTEGER, FOREIGN KEY(doctorid) REFERENCES doctors(doctorid), FOREIGN KEY(nurseid) REFERENCES nurses(nurseid))')
cur.execute('CREATE TABLE IF NOT EXISTS patient_files (patientid INTEGER, filename TEXT, FOREIGN KEY(patientid) REFERENCES patients(patientid))')

"""The code above does the following:
1. Connects to the database
2. Creates a cursor for the database
3. Executes a SQL statement to create a table named patients (if it doesn't already exist) with the columns patientid, room, name and DoctorID
4. Executes a SQL statement to create a table named doctors (if it doesn't already exist) with the columns doctorid and name
5. Executes a SQL statement to create a table named nurses (if it doesn't already exist) with the columns nurseid and name
6. Executes a SQL statement to create a table named medicines (if it doesn't already exist) with the columns pzn, name and price
7. Executes a SQL statement to create a table named patient_medicine (if it doesn't already exist) with the columns patientid and pzn
8. Executes a SQL statement to create a table named doctor_nurse (if it doesn't already exist) with the columns doctorid and nurseid
9. Executes a SQL statement to create a table named patient_files (if it doesn't already exist) with the columns patientid and filename"""

def add_patient(room, name, doctorid):
    # Adds a patient to the database 
    cur.execute('INSERT INTO patients (room, name, DoctorID) VALUES (?, ?, ?)', (room, name, doctorid))
    con.commit()

def add_doctor(name):
    # Adds a doctor to the database 
    cur.execute('INSERT INTO doctors (name) VALUES (?)', (name,))
    con.commit()

def add_nurse(name):
    # Adds a nurse to the database 
    cur.execute('INSERT INTO nurses (name) VALUES (?)', (name,))
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