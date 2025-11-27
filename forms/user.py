from flask_wtf import FlaskForm
from wtforms import (BooleanField, EmailField, IntegerField, PasswordField,
                     StringField, SubmitField)
from wtforms.validators import DataRequired


class UserLogin(FlaskForm):
    email = EmailField("Почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня", default=False)

    submit = SubmitField("Войти")
