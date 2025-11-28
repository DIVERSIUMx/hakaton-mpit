from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import (BooleanField, DateField, EmailField, FileField,
                     IntegerField, PasswordField, StringField, SubmitField,
                     TextAreaField)
from wtforms.validators import DataRequired


class NewsRedact(FlaskForm):
    name = StringField("Название", validators=[DataRequired()])
    body = TextAreaField("Содержание", validators=[DataRequired()])

    img = FileField("Картинка", validators=[
        FileAllowed(['jpg', 'png'])])

    submit = SubmitField("Применить")


class NewsAdd(FlaskForm):
    name = StringField("Название", validators=[DataRequired()])
    body = TextAreaField("Содержание", validators=[DataRequired()])

    img = FileField("Картинка", validators=[
        FileAllowed(['jpg', 'png']), DataRequired()])

    submit = SubmitField("Применить")
