from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  
            port=3307,         
            user='root',       
            password='Sn3461@#',  
            database='data'    
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Database connection error: {e}")
        return None


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/hello')
def hello():
    return 'Hello, world!'


@app.route('/users')
def users():
    conn = get_db_connection()  
    if conn is None:
        flash("Database connection error.", "error")
        return redirect(url_for('home'))

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM new_table")
        users_list = cursor.fetchall()
        return render_template('users.html', users=users_list)
    except Error as e:
        flash(f"Error fetching user list: {e}", "error")
        print(f"Query execution error: {e}")
        return render_template('error.html', error_message="Error fetching user list.")
    finally:
        cursor.close()
        conn.close()


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'GET':
        return render_template('new user.html')

    if request.method == 'POST':
        user_id = request.form['id']
        username = request.form['username']
        email = request.form['email']
        mobile = request.form['mobile']  

        
        if not user_id or not username or not email or not mobile:
            flash("All fields are required!", "error")
            return redirect(url_for('new_user'))

        conn = get_db_connection()
        if conn is None:
            flash("Database connection error.", "error")
            return redirect(url_for('new_user'))

        try:
            cursor = conn.cursor()

            
            cursor.execute("SELECT * FROM new_table WHERE email = %s", (email,))
            existing_user = cursor.fetchone()
            if existing_user:
                flash("Email is already in use.", "error")
                return redirect(url_for('new_user'))

            
            cursor.execute(
                "INSERT INTO new_table (ID, USERNAME, EMAIL, MOBILE) VALUES (%s, %s, %s, %s)",
                (user_id, username, email, mobile)
            )
            conn.commit()
            flash("User created successfully!", "success")
        except Error as e:
            flash(f"Database error: {e}", "error")
            print(f"Query execution error: {e}")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('new_user'))


@app.route('/users/<int:user_id>')
def user_detail(user_id):
    print(f"Fetching details for user with ID: {user_id}")  
    
    conn = get_db_connection()
    if conn is None:
        flash("Database connection error.", "error")
        print("Failed to connect to the database")  
        return redirect(url_for('home'))

    try:
        cursor = conn.cursor(dictionary=True)
        print(f"Executing query: SELECT * FROM new_table WHERE id = {user_id}") 
        
        cursor.execute("SELECT * FROM new_table WHERE id = %s", (user_id,))
        user = cursor.fetchone()

        if user is None:
            flash("User not found.", "error")
            print(f"No user found with ID: {user_id}")  
            return redirect(url_for('users'))

        print(f"User found: {user}")  
        return render_template('user_detail.html', user=user)
        
    except Error as e:
        flash(f"Error fetching user data: {e}", "error")
        print(f"Query execution error: {e}")  
        return render_template('error.html', error_message="Error fetching user data.")
        
    finally:
        cursor.close()
        conn.close()



if __name__ == "__main__":
    app.run(debug=True)
