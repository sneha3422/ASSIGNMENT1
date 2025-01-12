from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',         
        user='root',              
        password='Sn3461@#',      
        database='db1'            
    )
@app.route('/users')
def users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM USER")  
    users_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('users.html', users=users_list)

if __name__ == "__main__":
    app.run(debug=True)


