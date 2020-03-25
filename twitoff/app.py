"""Code for our app"""

# from decouple import config
from flask import Flask, render_template, request
from .models import DB
#making app factory

def create_app():
    app = Flask(__name__)

    #add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    #have the database know about this app
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='Home')
    return app

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset database!')
    return app
