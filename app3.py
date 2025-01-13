from flask import Flask, render_template, flash, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for flash messages

# Function to establish a database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',         
            user='root',
            password='Sn3461@#',      
            database='db3'            
        )
        if connection.is_connected():
            return connection
    except Error as e:
        flash(f"Error connecting to the database: {e}", "error")
        print(f"Database connection error: {e}")
        return None

# Route for displaying a single user's details
@app.route('/users/<int:id>')
def user_detail(id):
    conn = get_db_connection()
    if conn is None:
        return redirect(url_for('home'))  # Redirect to a safe route if connection fails

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM data WHERE id = %s", (id,))
        user = cursor.fetchone()
        cursor.close()
        
        if user is None:
            flash("User not found", "error")
            return redirect(url_for('users'))

        return render_template('user_detail.html', user=user)
    
    except Error as e:
        flash(f"Error fetching user data: {e}", "error")
        print(f"Error during query execution: {e}")
        return render_template('error.html', error_message="Error fetching user data.")
    
    finally:
        conn.close()

# Route for displaying all users
@app.route('/users')
def users():
    conn = get_db_connection()
    if conn is None:
        return redirect(url_for('home'))  # Redirect to a safe route if connection fails

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM data")
        users = cursor.fetchall()
        cursor.close()
        
        return render_template('users.html', users=users)
    
    except Error as e:
        flash(f"Error fetching user list: {e}", "error")
        print(f"Error during query execution: {e}")
        return render_template('error.html', error_message="Error fetching user list.")
    
    finally:
        conn.close()

# Home route
@app.route('/')
def home():
    return render_template('home.html')  # A simple home page to display when there's an error or on initial load

if __name__ == "__main__":
    app.run(debug=True)
