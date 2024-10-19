from flask import Flask, Blueprint, render_template, redirect, url_for
from apps.app import db
from apps.auth.models import User_auth
from apps.auth.forms import UserForm

login=Blueprint(
    "login", __name__,
    template_folder="template",
    static_folder="static"
)
@login.route("/")
def index():
    return render_template("login/test.html")