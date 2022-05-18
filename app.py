# from re import X
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin, LoginManager, login_required, login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from os import environ

from forms import ContactForm
from helper import get_files, get_blog_files, blogs_dict

uri = environ.get("DATABASE_URL")  # or other relevant config var
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = uri or 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

class ContactRequest(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), index = True)
    request = db.Column(db.String(1000))
    
class User(UserMixin, db.Model): #UserMixin only used on the User class
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), unique = True, index = True)
    password_hash = db.Column(db.String(128))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@app.route('/')
def index():
    col_one, col_two = get_files('home', 'main_page')
    return render_template('index.html', col_one = col_one, col_two = col_two)

@app.route('/<string:section>/<string:page>')
def basic(section, page):
    col_one, col_two = get_files(section, page.replace(' ', '_'))
    return render_template('basic.html', title=page, col_one = col_one, col_two = col_two)

@app.route('/<string:section>')
def menu(section):
    col_one, col_two = get_files(section, section.replace(' ', '_'))
    return render_template('menu.html', title=section, col_one = col_one, col_two = col_two)

@app.route('/blog/<string:page>')
def blog(page):
    page_info = get_blog_files(page)
    return render_template('blog.html', page_info = page_info)

@app.route('/blog')
def blog_menu():
    col_one, col_two = get_files('blog', 'blog')
    return render_template('blog_menu.html', col_one = col_one, col_two = col_two, blogs_dict = blogs_dict)

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            db.session.add(ContactRequest(name = form.name.data, 
                                            email = form.email.data, 
                                            request = form.request.data))
            db.session.commit()
            flash("Form entered successfully!")
            return redirect(url_for('contact', template_form = form))
    return render_template('contact.html', template_form = form, title='about & contact')

# db.create_all()