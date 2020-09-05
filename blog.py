from flask import Flask, render_template, url_for,flash ,redirect
from forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SECRET_KEY'] = '70759d00de48e536901b185e0d7f6efd'
app.config['SQLALCHMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


content = [
    {
        'author':'Ruan Pablo',
        'title':'First aplication in flask',
        'content':'Primeira aplicação zé',
        'date_posted':' Abril, 30, 2020'

    },
    {
        'author':'Maria Clara',
        'title':'Second aplication in flask',
        'content':'Segunda aplicação zé',
        'date_posted':' Abril, 31, 2020'

    },
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=content)


@app.route('/about')
def about_world():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('hello_world'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

