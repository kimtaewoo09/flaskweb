from flask import Flask, Blueprint, render_template, redirect, url_for
from app import db
from apps.board.models import Board
#from apps.board.forms import BoardForm
from flask_login import login_required

board=Blueprint(
    "board", __name__,
    template_folder="templates",
    static_folder="static")
@board.route("/")
def index():
    users=Board.query.all()
    return render_template("board/index.html")
