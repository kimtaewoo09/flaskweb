from flask import Flask, Blueprint, render_template, redirect, url_for
from apps.app import db
from apps.crud.models import User
from apps.crud.forms import UserForm

auth=Blueprint(
    "auth", __name__,
    template_folder="templates",
    static_folder="static"
)
@auth.route("/")
def index():
    return render_template("auth/test.html")