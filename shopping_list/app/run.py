
from flask import Flask
from flask_script import Manager
from flask_bootstrap import Bootstrap
from views import Register, Login

app = Flask(__name__)
app.config['SECRET_KEY'] = "iAMROOT"
manager = Manager(app)
bootstrap = Bootstrap(app)

app.add_url_rule('/register', view_func=Register.as_view('register'))
app.add_url_rule('/login', view_func=Login.as_view('login'))

if __name__ == "__main__":
    manager.run()
