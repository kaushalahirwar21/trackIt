from flask import Flask, render_template, request, redirect, url_for, session
import csv
import os
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

TEACHER_ID = 'admin'
TEACHER_PASSWORD = '123'

#---------- MySQL Setup ----------
conn = mysql.connector.connect(
    host='localhost',            # localhost
    user='root',
    password='1234', 
    database='student_db'  # <-- Ensure this DB exists
)
cursor = conn.cursor()

# ---------- Save to CSV ----------
def save_to_csv(data):
    filename = 'students.csv'
    file_exists = os.path.isfile(filename)
    serial_no = 1

    if file_exists:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            serial_no = sum(1 for row in reader)  # count rows (including header)

    with open(filename, 'a', newline='') as f:
        fieldnames = ['Serial No', 'Name', 'Roll Number', 'Course', 'Mobile Number', 'Timestamp']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            'Serial No': serial_no,
            'Name': data['name'],
            'Roll Number': data['roll'],
            'Course': data['course'],
            'Mobile Number': data['mobile'],
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

# ---------- Routes ----------
@app.route('/')
def index():
    return render_template('index.html')   #this

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        course = request.form['course']
        mobile = request.form['mobile']

        # Save to MySQL
        sql = "INSERT INTO students (name, roll, course, mobile) VALUES (%s, %s, %s, %s)"
        val = (name, roll, course, mobile)
        cursor.execute(sql, val)
        conn.commit()

        # Save to CSV
        save_to_csv({'name': name, 'roll': roll, 'course': course, 'mobile': mobile})

        return redirect(url_for('index'))  # Fix redirect

    return render_template('student.html')

@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == TEACHER_ID and password == TEACHER_PASSWORD:
            session['teacher_logged_in'] = True
            return redirect(url_for('student_details'))
        else:
            error = "Invalid ID or Password"
    return render_template('teacher.html', error=error)

@app.route('/student-details')
def student_details():
    if not session.get('teacher_logged_in'):
        return redirect(url_for('teacher'))

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    students = []
    for idx, row in enumerate(rows, start=1):
        students.append({
            'serial': idx,
            'name': row[1],
            'roll': row[2],
            'course': row[3],
            'mobile': row[4]
        })

    return render_template('student_details.html', students=students)

@app.route('/logout')
def logout():
    session.pop('teacher_logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
