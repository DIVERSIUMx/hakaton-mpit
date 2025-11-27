from flask_wtf import FlaskForm
from wtforms import (BooleanField, IntegerField, StringField, SubmitField,
                     TextAreaField)
from wtforms.validators import DataRequired, NumberRange


class CoureEditForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    desc = TextAreaField("Описание", validators=[DataRequired()])
    ball = StringField("Проходние баллы", validators=[DataRequired()])

    math = BooleanField("Математика", default=False)
    russian_lang = BooleanField("Русский язык", default=False)
    physics = BooleanField("Физика", default=False)
    it = BooleanField("Информатика", default=False)
    sosial = BooleanField("Обществознание", default=False)
    chemystry = BooleanField("Химия", default=False)
    liter = BooleanField("Литература", default=False)
    geography = BooleanField("География", default=False)
    forein_lang = BooleanField("Иностранный язык", default=False)

    submit = SubmitField("Применить")
