from flask import Flask, render_template
from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AOFMONKY'

class WTFform(FlaskForm):
    first_name = StringField("first_name", validators=[InputRequired()])
    last_name = StringField("last_name", validators=[InputRequired()])
    email = StringField("email", [InputRequired(""), Email("example@gmail.com")])
    username = StringField("username", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired(), Length(min=8, message="Password least 8 digits")])

@app.route('/')
def index():
    form = WTFform()
    return render_template('form.html', form=form)

@app.route('/registor', methods=["post"])
def registor():
    form = WTFform()
    if form.validate_on_submit():
        return "Registor SUCCESS!"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)