from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, SubmitField
from wtforms.validators import NumberRange


class CoureSerchForm(FlaskForm):
    by_name = StringField("По названию", validators=[])
    min_ball = StringField("от", validators=[])
    max_ball = StringField("до", validators=[])

    math = BooleanField("Математика", default=True)
    russian_lang = BooleanField("Русский язык", default=True)
    physics = BooleanField("Физика", default=True)
    it = BooleanField("Информатика", default=True)
    sosial = BooleanField("Обществознание", default=True)
    chemystry = BooleanField("Химия", default=True)
    liter = BooleanField("Литература", default=True)
    geography = BooleanField("География", default=True)
    forein_lang = BooleanField("Иностранный язык", default=True)

    submit = SubmitField("Найти")
