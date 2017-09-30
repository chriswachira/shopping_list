from flask import redirect, flash, make_response, render_template, url_for, session
from forms import RegistrationForm
from flask.views import View
from models import User, add_user

class Index(View):
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


