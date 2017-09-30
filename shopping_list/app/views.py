from flask import redirect, flash, make_response, render_template, url_for, session
from forms import RegistrationForm, LoginForm
from flask.views import View
from models import User, add_user, get_user

class Register(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        reg_form = RegistrationForm()
        if reg_form.validate_on_submit():
            user = User(reg_form.firstname.data,
                        reg_form.lastname.data,
                        reg_form.email.data,
                        reg_form.password.data)
            status = add_user(user.attribs)
            if status != None:
                flash("Email you entered is already registered!")

            else:
              #return redirect(url_for('dashboard'))
                flash('Successfully registered!')
                reg_form.firstname.data = ""
                reg_form.lastname.data = ""
                reg_form.email.data = ""
                reg_form.password.data = ""
                reg_form.password_confirm.data = ""

                #return url_for(Index)



        return render_template('signup.html', form=reg_form)


class Login(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        login_form = LoginForm()

        if login_form.validate_on_submit():
            search = get_user(login_form.username.data)

            if search != None:
                print("Search result: ", search)
                if login_form.password.data == search['pwd']:
                    flash('Logged in successfully!')
                    login_form.username.data = ""
                    login_form.password.data = ""
                else:
                    flash('Username or password incorrect!')
                    login_form.username.data = ""
                    login_form.password.data = ""
            else:
                flash('Username not found! Check again...')


        return render_template('login.html', form=login_form)
