from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    application.run(debug=True)