from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired



class UserNameForm(FlaskForm):
    userNameField = StringField("userNameField", validators=[DataRequired()])
    userSurNameField = StringField("userSurNameField", validators=[DataRequired()])     