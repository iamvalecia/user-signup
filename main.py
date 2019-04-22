from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup")
def display_sign_up_form():
    return render_template('sign_up.html')

#tests if input is an email. Emails contain '@' and '.'
#
def is_email(email):
    counter = 0
    for char in email:
        if "@" in char:
            counter = 1
    for char in email:
        if "." in char and counter == 1:
            return True

# Just KISS for these two functions. No need for else statements.
#tests if input is has space. No input should have a space.
#at the very char we detect " " this function stops to return True
def contains_space(string):
    for char in string:
        if " " in char:
            return True
        
@app.route("/signup", methods=['POST'])
def validate_sign_up_form():
    
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email_address']

    username_error= ""
    password_error= ""
    password2_error= ""
    email_error= ""

    if len(username) < 3 or len(username) > 20:
        username_error = "Username should be 3-20 characters."
    elif contains_space(username):
        username_error = "Username should not contain spaces."

    if len(password) < 3 or len(password) > 20:
        password_error = "Password should be 3-20 characters." 
    elif contains_space(password):
        password_error = "Password should not contain spaces."

    if password2 != password:
        password2_error = "Passwords must match."

    if not is_email(email) and email != "":
        email_error = "Not a valid email"
    elif contains_space(email) and email != "":
        email_error = "Email should not contain spaces."
    
    if not username_error and not password_error and not password2_error and not email_error:
        return render_template('welcome_page.html', name = username)
    else:
        return render_template('sign_up.html', 
        username_error=username_error,
        #lets the user's invalid input remain
        username=username,
        password_error=password_error,
        password2_error=password2_error,
        email_error=email_error,
        #lets the user's invalid input remain
        email=email)
        


#@app.route("/welcome_page", methods=['POST'])
#def welcome():
    #name = request.form['username']
    #return render_template('welcome_page.html', name=name) 

app.run()