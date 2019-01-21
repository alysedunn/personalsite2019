from flask import Flask, render_template

application = Flask(__name__)

FLASK_ENV = 'production'
FLASK_APP = 'Main/application.py'


@application.route('/')
def blog():
    return render_template('blog.html')


@application.route('/flask-aws')
def flask_aws():
    return render_template('flask_aws.html')


@application.route('/single')
def single():
    return render_template('single.html')


@application.route('/key_terms_and_definitions')
def key_terms_and_definitions():
    return render_template('key_terms_and_definitions.html')


if __name__ == "__main__":
    application.debug = False
    application.run()
