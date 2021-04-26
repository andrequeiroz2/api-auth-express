from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
from express.host.model import Host
from express.database import db


class HostForm(FlaskForm):
    hostname = StringField('Host', validators=[InputRequired()])
    submit = SubmitField('OK')

