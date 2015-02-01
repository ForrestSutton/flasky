from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtfoms.validators import DateRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
