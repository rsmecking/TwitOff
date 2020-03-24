from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(DB.Model):
    """Twitter users that we analyze"""
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(15), nullable=False)

class Tweet (DB.Model):
    """Tweets we pull"""
    id = db.Column(db.BigInteger, primary_key=True)
    text = db.Column(db.Unicode(280))
