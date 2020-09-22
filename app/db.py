from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
Column = db.Column
Integer = db.Integer
TIMESTAMP = db.TIMESTAMP
String = db.String
Relationship = db.relationship
ForeignKey = db.ForeignKey
BigInteger = db.BigInteger
Model = db.Model
Text = db.Text
session = db.session

