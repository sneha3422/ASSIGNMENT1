from flask import Flask, render_template, flash, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',         
            user='root',              
            password='Sn3461@#',      
            database='db1'            
        )
        if connection.is_connected():
            return connection
    except Error as e:
        flash(f"Error connecting to the database: {e}", "error")
        print(f"Error: {e}")
        return None


@app.route('/users')
def users():
    conn = get_db_connection()
    if conn is None:
        # If the connection fails, redirect to an error page or home page
        return redirect(url_for('home'))

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM USER")  # Adjust table name to be lowercase if needed
        users_list = cursor.fetchall()
        cursor.close()
        return render_template('users.html', users=users_list)
    
    except Error as e:
        flash(f"Error fetching data from the database: {e}", "error")
        print(f"Database query error: {e}")
        return render_template('error.html', error_message="Error fetching user data.")
    
    finally:
        conn.close()


@app.route('/')
def home():
    return render_template('home.html')  # A simple home page to redirect if there's an error


if __name__ == "__main__":
    app.run(debug=True)
