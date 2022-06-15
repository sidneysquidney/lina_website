from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from os import environ

from forms import ContactForm
from helper import get_files, get_blog_files, blogs_dict, pages, home, menus

uri = environ.get("DATABASE_URL")  # or other relevant config var
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = uri or 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# flask-mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sglethbridge@gmail.com'
app.config['MAIL_PASSWORD'] = 'ioqlewqpqrnquugl'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

class ContactRequest(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), index = True)
    request = db.Column(db.String(1000))
    
@app.route('/')
def index():
    col_one = {'home' + str(n): home[n] for n in range(len(home) // 2)}
    col_two = {'home' + str(n): home[n] for n in range(len(home) // 2, len(home))}
    return render_template('index.html', col_one = col_one, col_two = col_two)

@app.route('/<string:section>/<string:page>')
def basic(section, page):
    col_one = {page + str(n): pages[page][n] for n in range(len(pages[page]) // 2)}
    col_two = {page + str(n): pages[page][n] for n in range(len(pages[page]) // 2, len(pages[page]))}
    return render_template('basic.html', title=page, col_one = col_one, col_two = col_two)

@app.route('/<string:section>')
def menu(section):
    col_one = {menus[section][p][0]: menus[section][p][1] for p in range(len(menus[section]) // 2 )}
    col_two = {menus[section][p][0]: menus[section][p][1] for p in range(len(menus[section]) // 2 , len(menus[section]))}
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
            to_client = Message('Lina Katzmarcik Photography - Contact Confirmation', sender = 'sglethbridge@gmail.com', recipients = [form.email.data])
            to_me = Message('Lina Photography Inquiry', sender = 'sglethbridge@gmail.com', recipients = ['sglethbridge@gmail.com'])
            to_client.body = f"Dear {form.name.data}. \nThank you for getting in touch. We'll get back to you as soon as possible."
            to_me.body = f"From {form.name.data}, Email: {form.email.data}, Message: {form.request.data}"
            mail.send(to_client)
            mail.send(to_me)
            flash("Form entered successfully!")
            return redirect(url_for('contact', template_form = form))
    return render_template('contact.html', template_form = form, title='about & contact')