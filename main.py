import os

import dotenv
from flask import (Blueprint, Flask, abort, json, jsonify, make_response,
                   redirect, render_template, request)
from flask_login import LoginManager, current_user, login_user, logout_user
from PIL import Image

from data import db_session
from data.challenges import Chalange
from data.cources import Cource
from data.news import News
from data.user import User
from forms.cource import CoureAddForm, CoureEditForm
from forms.news import NewsRedact
from forms.serch import CoureSerchForm
from forms.user import UserLogin

app = Flask(__file__)

dotenv.load_dotenv()

app.config['SECRET_KEY'] = os.getenv("SECRET")

login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
@app.route("/index")
def index():
    db = db_session.create_session()
    news = db.query(News)
    cources = db.query(Cource)
    return render_template("index.html", title="index", current_user=current_user, news=news, cources=cources)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")
    form = UserLogin()

    if form.validate_on_submit():
        db = db_session.get_db().__next__()
        user = db.query(User).filter(User.email == form.email.data).first()
        if not user or not user.check_password(form.password.data):
            return render_template("login.html", message="Неверный логин или пароль", form=form, current_user=current_user)
        login_user(user, remember=form.remember_me.data)
        return redirect("/")

    return render_template("login.html", form=form, current_user=current_user)


@app.route("/cources", methods=["GET", "POST"])
def cources():
    form = CoureSerchForm()
    db = db_session.get_db().__next__()
    cources = db.query(Cource)
    print(form.by_name.data)
    if form.validate_on_submit():
        if form.by_name:
            cources = cources.filter(
                Cource.title.like(f"%{form.by_name.data}%"))
        if form.min_ball.data:
            if not form.min_ball.data.isnumeric():
                db.close()
                return render_template("cources.html", cources=cources, form=form, message="Минимальный бал должен быть числом", current_user=current_user)
            mi = int(form.min_ball.data)
            print(mi)
            cources = cources.filter(Cource.c_ball >= mi)
        if form.max_ball.data:

            if not form.max_ball.data.isnumeric():
                db.close()
                return render_template("cources.html", cources=cources, form=form, message="Максимальный бал должен быть числом", current_user=current_user)

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

    db.close()
    return render_template("cources.html", cources=cources, form=form, current_user=current_user)


@app.route("/cources/edit/<int:id>", methods=["GET", "POST"])
def cources_edit(id):
    if not current_user.is_authenticated:
        return redirect("/")

    db = db_session.create_session()
    cource = db.query(Cource).filter(Cource.id == id).first()

    if not cource:
        return abort(404)

    form = CoureEditForm()

    if form.validate_on_submit():
        cource.title = form.title.data
        cource.desc = form.desc.data
        cource.c_ball = form.ball.data

        cource.math = form.math.data
        cource.russian_lang = form.russian_lang.data
        cource.physics = form.physics.data
        cource.it = form.it.data
        cource.sosial = form.sosial.data
        cource.chemystry = form.chemystry.data
        cource.liter = form.liter.data
        cource.geography = form.geography.data
        cource.forein_lang = form.forein_lang.data

        db.commit()
        return redirect("/cources")

    form.title.data = cource.title
    form.desc.data = cource.desc
    form.ball.data = cource.c_ball

    form.math.data = cource.math
    form.russian_lang.data = cource.russian_lang
    form.physics.data = cource.physics
    form.it.data = cource.it
    form.sosial.data = cource.sosial
    form.chemystry.data = cource.chemystry
    form.liter.data = cource.liter
    form.geography.data = cource.geography
    form.forein_lang.data = cource.forein_lang

    return render_template("cource_edit.html", current_user=current_user, form=form, cource_id=cource.id)


@app.route("/cources/edit/<int:id>/delete")
def delete_couse(id):
    if not current_user.is_authenticated:
        return redirect("/cources")

    db = db_session.create_session()

    cource = db.query(Cource).filter(Cource.id == id).first()

    if cource:
        db.delete(cource)
        db.commit()

    db.close()
    return redirect("/cources")


@app.route("/cources/edit/new", methods=["GET", "POST"])
def new_cource():
    if not current_user.is_authenticated:
        return redirect("/cources")

    form = CoureAddForm()

    if form.validate_on_submit():
        cource = Cource()
        cource.title = form.title.data
        cource.desc = form.desc.data
        cource.c_ball = form.ball.data

        cource.math = form.math.data
        cource.russian_lang = form.russian_lang.data
        cource.physics = form.physics.data
        cource.it = form.it.data
        cource.sosial = form.sosial.data
        cource.chemystry = form.chemystry.data
        cource.liter = form.liter.data
        cource.geography = form.geography.data
        cource.forein_lang = form.forein_lang.data

        db = db_session.create_session()
        db.add(cource)
        db.commit()
        db.close()
        return redirect("/cources")

    return render_template("cource_add.html", form=form)


@app.route("/news/edit/<int:id>", methods=["GET", "POST"])
def news_edit(id):
    if not current_user.is_authenticated:
        return redirect("/")

    db = db_session.create_session()
    news = db.query(News).filter(News.id == id).first()

    if not news:
        return abort(404)

    form = NewsRedact()

    if form.validate_on_submit():
        if form.img.data:
            f = Image.open(form.img.data)
            f.save(f"./static/img/news/{news.img}")

        news.name = form.name.data
        news.body = form.body.data

        db.commit()
        db.close()
        return redirect("/merch")

    form.name.data = news.name
    form.body.data = news.body
    img = news.img

    return render_template("news_edit.html", news_id=id, img=img, form=form)


@app.route("/news/edit/new", methods=["GET", "POST"])
def news_add():
    if not current_user.is_authenticated:
        return redirect("/")

    form = NewsRedact()

    if form.validate_on_submit():
        db = db_session.create_session()
        news = News()

        news.name = form.name.data
        news.body = form.body.data

        files = os.listdir(os.path.join("static", "img", "news"))

        if not files:
            filename = "1.png"
        else:
            filename = f"{max(map(lambda f: int(f.split(".")[0]), files)) + 1}.png"

        f = Image.open(form.img.data)
        f.convert
        f.save(os.path.join("static", "img", "news", filename))
        news.img = filename
        db.add(news)
        db.commit()
        db.close()
        return redirect("/merch")

    return render_template("news_add.html", news_id=id, form=form)


@app.route("/news/delete/<int:id>")
def news_delete(id):
    if not current_user.is_authenticated:
        return redirect("/")

    db = db_session.create_session()
    news = db.query(News).filter(News.id == id).first()

    if not news:
        return abort(404)

    db.delete(news)
    db.commit()
    db.close()

    return redirect("/merch")


@app.route("/merch")
def merch():
    db = db_session.create_session()
    news = db.query(News)
    return render_template("merch.html", news=news, current_user=current_user)


@app.route("/api/get-avalable-cources")
def get_cources():
    ball_ctn = request.args.get("ball_ctn")

    if not ball_ctn or not ball_ctn.isnumeric():
        return make_response({"error": "Bad request"}, 400)

    db = db_session.create_session()

    c = db.query(Cource).filter(Cource.c_ball <= int(ball_ctn))
    if not request.args.get("math"):
        c = c.filter(Cource.math == 0)

    if not request.args.get("it"):
        c = c.filter(Cource.it == 0)

    if not request.args.get("chemystry"):
        c = c.filter(Cource.chemystry == 0)

    if not request.args.get("sosial"):
        c = c.filter(Cource.sosial == 0)

    if not request.args.get("physics"):
        c = c.filter(Cource.physics == 0)

    if not request.args.get("russian_lang"):
        c = c.filter(Cource.russian_lang == 0)

    if not request.args.get("geography"):
        c = c.filter(Cource.geography == 0)

    if not request.args.get("liter"):
        c = c.filter(Cource.liter == 0)

    return make_response(jsonify([cource.to_dict() for cource in c]), 200)


@app.route("/calc")
def calc():
    return render_template("calc.html")


@login_manager.user_loader
def load_user(id):
    db = db_session.create_session()
    return db.query(User).get(id)


def main():
    db_session.global_init("./db/blob.db")
    db = db_session.create_session()
    if not db.query(User).get(1):
        user = User()
        user.name = "admin"
        user.second_name = "admin"
        user.email = "t@t.org"
        user.set_password("123")
        db.add(user)
        db.commit()
    db.close()
    app.run("127.0.0.1", 8080)


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    main()
