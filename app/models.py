from app import bcrypt

import datetime, time

from config import WHOOSH_ENABLED

enable_search = WHOOSH_ENABLED
if enable_search:
    import flask_whooshalchemy as whooshalchemy


""" 
For reference
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=False)
    last_name = db.Column(db.String(64), index=True, unique=False)
    item = db.Column(db.String(140))
    duration = db.Column(db.Integer, index=True)
    dueDate = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime)
    days_remaining = db.Column(db.Integer)
    tech = db.Column(db.String(64))

    def __repr__(self):
        return '<Entry %r>' % (self.first_name)
    
    #def __init__(self, first_name, last_name, body):
     #   self.first_name=first_name
    #  self.last_name = last_name
       # self.body = body
        
    def getPrintableDueDate(self):
        return self.dueDate.strftime('%d/%m/%Y')

"""
