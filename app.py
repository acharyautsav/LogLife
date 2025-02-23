from flask import Flask, jsonify, render_template, request
import mysql.connector
import pymysql
from db import get_db_connection
from db import getpy_db_connection
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash



app = Flask(__name__)


@app.route('/')
def loginmain():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('landing_page.html')

@app.route('/to_do_list')
def to_do_list():
    return render_template('to_do_list.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')

@app.route('/daily_journal')
def daily_journal():
    return render_template('daily_journal.html')

@app.route('/landing_page')
def landing_page():
    return render_template('landing_page.html')

@app.route('/submit_journal', methods=['POST'])
def submit_journal():
    # Get the JSON data from the request
    data = request.get_json()
    
    date = data['date']
    day = data['day']
    productivity = data['productivity']
    mood = data['mood']
    went_well = data['went_well']
    went_wrong = data['went_wrong']
    thoughts = data['thoughts']
    todo_lists = data['todo_lists']

    # Insert into MySQL
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO journal_entries (date, day, productivity, mood, went_well, went_wrong, thoughts, todo_lists) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', 
                   (date, day, productivity, mood, went_well, went_wrong, thoughts, todo_lists))
    conn.commit()
    cursor.close()
    conn.close()
    
    # Return a JSON response indicating success
    return jsonify({"message": "Journal entry submitted successfully!"})

@app.route('/login', methods=['POST'])
def login():
    # Get data from the frontend (JSON format)
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not email or not password:
        return jsonify({'success': False, 'message': 'Missing email or password'}), 400

    # Initialize connection and cursor to None
    conn = None
    cursor = None
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Query the database to find the user with the provided email
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()

        # Check if the user exists and the password is correct (no hashing)
        if user and user['password_hash'] == password:  # Compare plain-text passwords directly
            return jsonify({'success': True, 'message': 'Login successful'})
        else:
            return jsonify({'success': False, 'message': 'Invalid email or password'}), 401
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({'success': False, 'message': 'Database error'}), 500
    finally:
        # Always close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    # Get data from the frontend (assuming JSON format)
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')

    # Validate the input data
    if not email or not password or not first_name:
        return jsonify({"success": False, "message": "Missing required fields"}), 400

    # Connect to the database and insert the new user
    conn = getpy_db_connection()
    cursor = conn.cursor()

    try:
        # Insert user data into the 'users' table (without password hashing)
        cursor.execute('''INSERT INTO users (email, password_hash, first_name) 
                          VALUES (%s, %s, %s)''', 
                       (email, password, first_name))
        conn.commit()  # Commit the transaction
        return jsonify({"success": True, "message": "User registered successfully!"}), 201

    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": f"Error: {err}"}), 500

    finally:
        # Close the connection
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
