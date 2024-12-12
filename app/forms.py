from flask_appbuilder.forms import DynamicForm
from flask_wtf import RecaptchaField
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
)


class ContactForm(DynamicForm):
    name = StringField("Name")
    email = StringField("Email")
    message = TextAreaField("Message")
    recaptcha = RecaptchaField()
    submit = SubmitField(label="Submit")
