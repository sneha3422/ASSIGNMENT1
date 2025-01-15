TASK1:FLASK API DEVELOPMENT

Table of Contents
Prerequisites
Setting up Flask Environment
MySQL Setup
File names
Implemented Routes
/hello route
/users route
/new_user route
/users/<id> route
Error Handling
Testing and Running the Application
Conclusion

Prerequisites
Python 3.x: Install Python 3.x from the official Python website (https://www.python.org/downloads/).
MySQL Community Edition: Download and install the MySQL Community Edition (https://dev.mysql.com/downloads/installer/).
MySQL Workbench: For managing my MySQL database,  I download and install MySQL Workbench (https://dev.mysql.com/downloads/workbench/).

Setting up Flask Environment
1. Install Python 3.x:
Install Python 3.x on my system. 

2. Install Flask using pip:
Once Python is installed, open the terminal and run the following command to install Flask:
pip install Flask

3. Set up Virtual Environment:
I activate and create virtual environment with the python -m venv env command.


4. Install MySQL Connector:
To connect Flask with MySQL, I install the MySQL connector by using pip install mysql-connector-python command


MySQL Setup
1. Install MySQL Community Edition:
Download and install the MySQL Community Edition from the official site.
During the installation, set up the root password and select Port 3306 as the default connection port.
2. Install MySQL Workbench:
Download and install MySQL Workbench to interact with your MySQL server.
3. Set up MySQL Database:
Open MySQL Workbench and connect to my MySQL server using the root username and the password you set during installation.
Create a new database (e.g., db1) and add a users table with the necessary fields (e.g., id, name, email, password).
   
File names  :
main.py
app.py
app2.py
app3.py


Implemented Routes
1. /hello Route
This route displays a simple "Hello World" message when accessed.

2. /users Route
This route retrieves a list of users from the MySQL database and displays them in an HTML table.

3. /new_user Route
This route renders an HTML page to accept user input for creating a new user and stores the information in the database.

4. /users/<id> Route
This route retrieves the details of a specific user by their ID from the database.

Error Handling
Proper error handling is implemented in each route to ensure that if there is a failure in the database connection or
any unexpected errors, the user will see an appropriate error message, and they will be redirected to the home page.

Testing and Running the Application by:
Open a terminal and navigate to the Flask app directory.
Run the Flask application:
Access the routes using the following URLs:
http://127.0.0.1:5000/hello – Displays "Hello World!"
http://127.0.0.1:5000/users – Displays a list of users from the database.
http://127.0.0.1:5000/new_user – Displays the form to create a new user.
http://127.0.0.1:5000/users/<id> – Displays details of a specific user.

Conclusion
This documentation provides a step-by-step guide to how do I set up a Flask application that integrates with a MySQL database.
The application demonstrates how to manage users by creating routes for displaying users, adding new users, and viewing specific user details.
Error handling ensures that the application is robust and can handle common database connection failures.







TASK1:FLASK API DEVELOPMENT

Table of Contents
Prerequisites
Setting up Flask Environment
MySQL Setup
File names
Implemented Routes
/hello route
/users route
/new_user route
/users/<id> route
Error Handling
Testing and Running the Application
Conclusion

Prerequisites
Python 3.x: Install Python 3.x from the official Python website (https://www.python.org/downloads/).
MySQL Community Edition: Download and install the MySQL Community Edition (https://dev.mysql.com/downloads/installer/).
MySQL Workbench: For managing my MySQL database,  I download and install MySQL Workbench (https://dev.mysql.com/downloads/workbench/).

Setting up Flask Environment
1. Install Python 3.x:
Install Python 3.x on my system. 

2. Install Flask using pip:
Once Python is installed, open the terminal and run the following command to install Flask:
pip install Flask

3. Set up Virtual Environment:
I activate and create virtual environment with the python -m venv env command.


4. Install MySQL Connector:
To connect Flask with MySQL, I install the MySQL connector by using pip install mysql-connector-python command


MySQL Setup
1. Install MySQL Community Edition:
Download and install the MySQL Community Edition from the official site.
During the installation, set up the root password and select Port 3306 as the default connection port.
2. Install MySQL Workbench:
Download and install MySQL Workbench to interact with your MySQL server.
3. Set up MySQL Database:
Open MySQL Workbench and connect to my MySQL server using the root username and the password you set during installation.
Create a new database (e.g., db1) and add a users table with the necessary fields (e.g., id, name, email, password).
   
File names  :
main.py
app.py
app2.py
app3.py


Implemented Routes
1. /hello Route
This route displays a simple "Hello World" message when accessed.

2. /users Route
This route retrieves a list of users from the MySQL database and displays them in an HTML table.

3. /new_user Route
This route renders an HTML page to accept user input for creating a new user and stores the information in the database.

4. /users/<id> Route
This route retrieves the details of a specific user by their ID from the database.

Error Handling
Proper error handling is implemented in each route to ensure that if there is a failure in the database connection or
any unexpected errors, the user will see an appropriate error message, and they will be redirected to the home page.

Testing and Running the Application by:
Open a terminal and navigate to the Flask app directory.
Run the Flask application:
Access the routes using the following URLs:
http://127.0.0.1:5000/hello – Displays "Hello World!"
http://127.0.0.1:5000/users – Displays a list of users from the database.
http://127.0.0.1:5000/new_user – Displays the form to create a new user.
http://127.0.0.1:5000/users/<id> – Displays details of a specific user.

Conclusion
This documentation provides a step-by-step guide to how do I set up a Flask application that integrates with a MySQL database.
The application demonstrates how to manage users by creating routes for displaying users, adding new users, and viewing specific user details.
Error handling ensures that the application is robust and can handle common database connection failures.

TASK2: DATABASE INTERACTION
Prerequisites
MySQL Community Server
MySQL Workbench


Step 1: Install MySQL Community Server
I Go to the official MySQL download page:
Then Download MySQL Community Server
Download the appropriate installer for my operating system.
Run the installer and follow the steps. During installation:
Choose the Server only option.
Set a root password that I will use later to connect to MySQL.
Complete the installation.

Step 2: Install MySQL Workbench
Download MySQL Workbench from:
Download MySQL Workbench
Follow the installation instructions specific to my operating system.

Step 3: Configure MySQL Server with Password and Port
Open MySQL Workbench after installation.
In the MySQL Connections panel, click the "+" symbol to create a new connection.
In the Setup New Connection window:
Connection Name: Local instance MySQL91
Connection Method:  Standard (TCP/IP).
Hostname: localhost.
Port: Default port is 3307 
Username: root
Password: Sn3461@#
Click OK to save and connect to my MySQL server.
Database Creation

Step 4: Create the Datababase connection 
My database name is data and

Step 5: Create Table user
Now, create a table named user in the data database with the following specifications:

id: Auto-incremented, primary key, and not null.
name: Not null.
email: Not null.
First, switch to the users database:

Step 6: Insert Data into user Table
Next, insert sample data into the user table.
then my table is created.

GIT WORKFLOW AND ITS CONTRIBUTION TO PROJECT:

Prerequisites
Git: Install Git by downloading it from Git's official website.
GitHub Account: Create an account on GitHub 
Flask Project Folder:Flask project files.

Steps for GitHub Workflow
Step 1: Install Git
Download and install Git from Git Downloads.
During installation, select Git Bash to be installed.

Step 2: Create a GitHub Account and Repository
Create a GitHub account with the username sneha3422  at GitHub Sign-Up.
After logging in to GitHub, go to my GitHub Dashboard and click on the + icon in the upper right corner.
Select New Repository.
Repository Name: Name my repository ASSIGNMENT1.
Optionally, add a description for my repository.
Choose the repository public.
Click Create Repository to complete the process.

Step 3: Initialize Git in my Local Flask Folder
Navigate to the folder where my Flask project files are stored .
Right-click inside the folder and select Git Bash Here (this opens the Git Bash terminal).
In the Git Bash terminal, run the following command to initialize Git in my folder:
git init
This command initializes an empty Git repository in my project folder.

Step 4: Add Files to Git
To add all the files in my flask project folder to the Git staging area, run the following command:
git add .
The git add . command stages all the files in the folder for committing.

Step 5: Commit Changes
After adding files, it's time to commit the changes. Run the following command to commit:
git commit -m "files added"
Here, "files added" is the commit message. 

Step 6: Link my Local Repository to GitHub
Go to my GitHub repository page  https://github.com/sneha3422/ASSIGNMENT1
Copy the repository URL  https://github.com/sneha3422/ASSIGNMENT1.git
Go back to my Git Bash terminal and link my local repository to the GitHub repository by running the following command:
git remote add origin https://github.com/sneha3422/ASSIGNMENT1.git

Step 7: Push my Local Repository to GitHub
To push my local commits to the GitHub repository, run the following command:
git push -u origin master
This command uploads my local project files to the GitHub repository. 








