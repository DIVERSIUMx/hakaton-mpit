import os

import dotenv
from flask import Blueprint, Flask, redirect, render_template, request
from flask_login import current_user

from data import db_session
from data.challenges import Chalange
from data.cources import Cource
from forms.serch import CoureSerchForm

app = Flask(__file__)

dotenv.load_dotenv()

app.config['SECRET_KEY'] = os.getenv("SECRET")


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="index", current_user=current_user)


@app.route("/cources", methods=["GET", "POST"])
def cources():
    form = CoureSerchForm()
    db = db_session.create_session()
    cources = db.query(Cource)
    print(form.by_name.data)
    if form.validate_on_submit():
        if form.by_name:
            cources = cources.filter(
                Cource.title.like(f"%{form.by_name.data}%"))
        if form.min_ball.data:
            if not form.min_ball.data.isnumeric():
                return render_template("cources.html", cources=cources, form=form, message="Минимальный бал должен быть числом")
            mi = int(form.min_ball.data)
            print(mi)
            cources = cources.filter(Cource.c_ball >= mi)
        if form.max_ball.data:

            if not form.max_ball.data.isnumeric():
                return render_template("cources.html", cources=cources, form=form, message="Максимальный бал должен быть числом")

            ma = int(form.max_ball.data)
            cources = cources.filter(Cource.c_ball <= ma)

        if any([form.math.data, form.russian_lang.data, form.physics.data, form.it.data, form.sosial.data, form.chemystry.data, form.liter.data, form.geography.data, form.forein_lang.data]):
            if form.math.data:
                cources = cources.filter(Cource.math)
            if form.russian_lang.data:
                cources = cources.filter(Cource.russian_lang)
            if form.physics.data:
                cources = cources.filter(Cource.physics)
            if form.it.data:
                cources = cources.filter(Cource.it)
            if form.sosial.data:
                cources = cources.filter(Cource.sosial)
            if form.chemystry.data:
                cources = cources.filter(Cource.chemystry)
            if form.liter.data:
                cources = cources.filter(Cource.liter)
            if form.geography.data:
                cources = cources.filter(Cource.geography)
            if form.forein_lang.data:
                cources = cources.filter(Cource.forein_lang)

    return render_template("cources.html", cources=cources, form=form)


def main():
    db_session.global_init("./db/blob.db")
    app.run("127.0.0.1", 8080)


if __name__ == "__main__":
    main()
