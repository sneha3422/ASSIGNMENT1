from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector
from mysql.connector import Error



app = Flask(__name__)
app.secret_key = 'your_secret_key'



def get_db_connection(database_name):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Sn3461@#',
            database=database_name
        )
        if connection.is_connected():
            return connection
    except Error as e:
        flash(f"Database connection error: {e}", "error")
        print(f"Error: {e}")
        return None

@app.route('/hello')
def hello():
    return 'Hello world!'

@app.route('/users')
def users():
    conn = get_db_connection("db1")
    if conn is None:
        return redirect(url_for('home'))

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM USER") 
        users_list = cursor.fetchall()
        cursor.close()
        return render_template('users.html', users=users_list)
    except Error as e:
        flash(f"Error fetching user list: {e}", "error")
        print(f"Error during query execution: {e}")
        return render_template('error.html', error_message="Error fetching user list.")
    finally:
        conn.close()


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'GET':
        return render_template('new user.html')

    if request.method == 'POST':
        id = request.form['id']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not id or not username or not email or not password:
            flash("All fields are required!", "error")
            return redirect(url_for('new_user'))

        hashed_password = generate_password_hash(password)

        try:
            conn = get_db_connection("db2")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM new_user WHERE email = %s", (email,))
            existing_user = cursor.fetchone()
            if existing_user:
                flash("Email is already in use.", "error")
                return redirect(url_for('new_user'))

            cursor.execute("INSERT INTO new_user (ID, USERNAME, EMAIL, PASSWORD) VALUES (%s, %s, %s, %s)",
                           (id, username, email, hashed_password))
            conn.commit()
            flash("User created successfully!", "success")
        except Error as e:
            flash(f"Database error: {e}", "error")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('new_user'))



@app.route('/users/<int:id>')
def user_detail(id):
    conn = get_db_connection("db3")
    if conn is None:
        return redirect(url_for('home'))

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



@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)