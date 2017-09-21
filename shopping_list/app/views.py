from flask import render_template
from app import app
#from flask.ext.wtf import Form
#from wtforms import StringField, SubmitField
#from wtforms.validatoes import Required

#@app.route('/')
#def index():
 #   return "Hello, World!"

@app.route('/login')
def login():
    return render_template("sign_in.html")

@app.route('/signup')
def sign_in():
    return render_template("sign_up.html")

@app.route('/dashboard')
def dashboard():
    #return render_template("dashboard.html")
    return render_template("dashboard.html")
#class LoginForm(Form):
 #   username = StringField("Username:", validators=[Required()])
  #  password = PasswordField("Password: ", validators=[Required()])
