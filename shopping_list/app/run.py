
from flask import Flask
from flask_script import Manager
from flask_bootstrap import Bootstrap
from views import Index

app = Flask(__name__)
app.config['SECRET_KEY'] = "iAMROOT"
manager = Manager(app)
bootstrap = Bootstrap(app)

app.add_url_rule('/', view_func=Index.as_view('index'))

if __name__ == "__main__":
    manager.run()
