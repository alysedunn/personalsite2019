from flask import Flask, redirect, render_template, url_for

application = Flask(__name__)

FLASK_ENV = 'production'
FLASK_APP = 'Main/application.py'


@application.route('/')
@application.route('/blog/technology-and-programming')
def home():
    return redirect(url_for('blog'))


@application.route('/blog')
def blog():
    return render_template('blog.html')


@application.route('/blog/technology-and-programming/flask-aws')
def flask_aws():
    return render_template('flask_aws.html')


@application.route('/key-terms-and-definitions')
def key_terms_and_definitions():
    return render_template('key_terms_and_definitions.html')


@application.route('/blog/technology-and-programming/novice-newcomer-to-professional-programmer')
def novice_newcomer_to_professional_programmer():
    return render_template('novice_newcomer_to_professional_programmer.html')


@application.route('/blog/single')
def single():
    return render_template('single.html')


if __name__ == "__main__":
    application.debug = False
    application.run()
