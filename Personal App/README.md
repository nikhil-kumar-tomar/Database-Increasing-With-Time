# Introduction
This is a Project for web development. This whole web app is designed using Django Framework in Python. The best and the most powerful Technology used in this web app is Object Relational Mapper provided by Django that allows easy manipulation of Databases.
 
This project mainly focuses on combining Frontend and Backend as to let the user or clients do Create, Read, Update and Delete operations directly on the Database.
 
The HTML used in this project is not pure HTML, but rather templates of HTML that can be easily read and transformed by Django.
 
This web app represents a simple implementation of CRUD operations, so I have not spent much time on the Frontend of this project.
Although I am giving some time to Frontend, But I spent most of my time fixing Bugs and Enhancing Security and Verification of this web app.
 
For the web app to work, It requires a MySQL Database with configuration provided. Getting on to main Web pages.it shows Choices which can be selected one by one, The choices include the following:
 
# 1. See all Students in the Database
This option shows all the available Records in a beautiful Dark Bootstrap Table.
 
# 2. Search Specific Student
This option requires the roll number of the student to see his/her details, these details are also shown in a Dark Bootstrap Table.
 
# 3. Enter Information to create Record of a Student
This option require Roll Number, Name and Email, Basically all the information for a Student, Simple Django forms are used here and off course a CSRF tag for security is also used in all the forms and inputs I have used.
 
# 4. Update already existing Record of a Student
This option requires a roll number, filling roll number will show pre-populated form fields with information already available in the database, updating this fields and submitting will affect the database.
 
 
# Configuration for Backend applications# Django Admin Page

admin page at: localhost:8000/admin

Username: admin

Password: Nick@123
 
 
# MySQL Database configurations
Database Name: personal

Database User: root

Database Password: 123456789

Database Host: localhost

Database Port: 3306
 
 
# Extras
For this Project I have also provided a Virtual Environment of Python using Pipenv, This virtual environment can be easily used without installing every package used in this project.