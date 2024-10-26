from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request
from app import db
from apps.crud.models import User
from apps.login.forms import SignUpForm
from flask_login import login_user, logout_user

login=Blueprint(
    "login", __name__,
    template_folder="template",
    static_folder="static"
)
@login.route("/")
def index():
    return render_template("login/index.html")
@login.route("/signup", methods=["GET","POST"])
def signup():
    form=SignUpForm()
    if form.validate_on_submit():
        user= User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        if user.is_duplicate_email():
            flash("지정한 이메일 주소는 이미 등록되어있습니다")
            return redirect(url_for("login.signup"))
        db.session.add(user)
        db.session.commit()

        login_user(user)

        next_=request.args.get("next")
        if next_ is None and not next_.startswith("/"):
            next_=url_for("crud.users")
        return redirect(next_)
    return render_template("login/signup.html", form=form)
'''@login.route("/login",method=["GET","POST"])
def login():
    form = LoginForm'''