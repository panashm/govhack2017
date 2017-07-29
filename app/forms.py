from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf import Form
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField, SelectField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email
from wtforms.widgets import TextArea

"""
item_choices = [ (0, 'VGA Adapter'),(1, 'Apple Superdrive'),(2, 'T430'), (3, 'Other') ]

For reference purposes
class newEntryForm(Form):
    firstName = TextField('Enter first Name:', validators=[Required()])
    lastName = TextField('Enter last Name:', validators=[Required()])
    body = TextField(u'Text', widget=TextArea(), validators=[Required()])
    item = SelectField('Select Item:',
                            [validators.Required()],
                            choices=item_choices)
    duration = SelectField('Duration (Days):',
                            [validators.Required()],
                            choices=day_choices)
    
"""