
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail



app_ = Flask(__name__)
app_.config['SECRET_KEY'] = 'e87aab13814946b97df9c1712a6937f6'
app_.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db_ = SQLAlchemy(app_)
bcrypt = Bcrypt(app_)
login_manager = LoginManager(app_)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app_.config['MAIL_SERVER'] = 'smtp.zoho.com'
app_.config['MAIL_PORT'] = 587
app_.config['MAIL_USE_TLS'] = True
#.bash did not work I had to hardcode credentials
app_.config['MAIL_USERNAME'] = 'info@womeninrpa.com'
app_.config['MAIL_PASSWORD'] = 'wilfred1989X!'
#app_.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
#app_.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app_)

#print("Email User:", app_.config['MAIL_USERNAME'])
#print("Email Pass:", os.environ.get('EMAIL_PASS'))

from Corey_v2_package.flask_app import routes




