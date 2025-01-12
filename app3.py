from flask import Flask, render_template, flash, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  



def get_db_connection():
    return mysql.connector.connect(
        host='localhost',         
        user='root',
        password='Sn3461@#',      
        database='db3'            
    )


@app.route('/users/<int:id>')
def user_detail(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    
    cursor.execute("SELECT * FROM data WHERE id = %s", (id,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()

    
    if user is None:
        flash("User not found", "error")
        return redirect(url_for('users'))  

    
    return render_template('user_detail.html', user=user)


@app.route('/users')
def users():
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    
    cursor.execute("SELECT * FROM data")
    users = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    
    return render_template('user_detail.html', user=users)


if __name__ == "__main__":
    app.run(debug=True)
