from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Organization(db.Model):
    __tablename__ = 'organization'
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.String(256))

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.String(80))
