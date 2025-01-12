from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Sn3461@#',
        database='db2'
    )


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'GET':
        
        return render_template('new user.html')  
    
    if request.method == 'POST':
        
        id =request.form['id']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if not id or not username or not email or not password:
            flash("All fields are required!", "error")
            return redirect(url_for('new_user'))
        
        
        hashed_password = generate_password_hash(password)
        
        try:
    
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute("INSERT INTO new_table (id, username, email, password) VALUES (%s, %s, %s)", 
                           (id, username, email, hashed_password))
            conn.commit()  
            
        
            flash("User created successfully!", "success")
        except mysql.connector.Error as err:
            flash(f"Error: {err}", "error")
        finally:
            cursor.close()
            conn.close()
        
        # Redirect to the '/users' page after the user has been added
        return redirect(url_for('new_user'))

# Route to handle the '/users' page (list of users, for example)

if __name__ == "__main__":
    app.run(debug=True)
