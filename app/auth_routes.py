from flask import Blueprint, render_template, url_for, flash, redirect, request
from app import db
from app.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

bcrypt = Bcrypt() # Inicialize Bcrypt aqui

@auth.route("/", methods=["GET"])
def index():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    return render_template("index.html", title="Início")

@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Sua conta foi criada com sucesso! Agora você pode fazer login.", "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html", title="Cadastro", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=False)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.dashboard"))
        else:
            flash("Login sem sucesso. Por favor, verifique seu email e senha", "danger")
    return render_template("login.html", title="Login", form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
