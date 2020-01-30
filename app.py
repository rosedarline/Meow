from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'
if ENV == 'dev':
     app.debug = True
     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost/Meow'
else:
     app.debug = False
     app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_DATABASE_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Meow(db.Model):
    __tablename__ = 'meow'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(200))
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    email = db.Column(db.String(200))
    
    def __init__(self, gender, firstname, lastname, email):
        self.gender = gender
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


@app.route('/')
def index():
    print('Hello Wolrd!')
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        gender = request.form['gender']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        print(gender, firstname, lastname, email)
        if gender == '' or firstname == '':
            return render_template('index.html', message ='Please enter required fields')
        data = Meow(gender, firstname, lastname, email)
        db.session.add(data)
        db.session.commit()
        return render_template('index.html')
    return 'Nope.'


if __name__ == '__main__':
    app.run()
