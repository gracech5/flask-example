from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
application = Flask(__name__)

application.config['SECRET_KEY'] = 'mykey'

class SimpleForm(FlaskForm):
    name = StringField('Name: ')
    age = StringField('Age: ')
    gender = SelectField('Gender: ', choices=[('male', 'Male'), ('female', 'Female')])


@application.route('/')
def index():
    return render_template('index.html')

@application.route('/register', methods=['POST','GET'])
def register():
    form = SimpleForm()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        gender = form.gender.data
        return redirect(url_for('submitted', name=name, age=age, gender=gender))
    return render_template('register.html', form=form)

@application.route('/submitted')
def submitted():
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    return render_template('submitted.html', name=name, age=age, gender=gender)


if __name__ == '__main__':
    application.run(debug=True)