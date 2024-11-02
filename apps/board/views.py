from flask import Flask, Blueprint, render_template, redirect, url_for
from app import db
from apps.board.models import Board
from apps.board.forms import BoardForm
from flask_login import login_required

board=Blueprint(
    "board", __name__,
    template_folder="templates",
    static_folder="static")
@board.route("/")
def index():
    users=Board.query.all()
    return render_template("board/index.html")
@board.route('/users/new',methods=["GET","POST"])
def create_user(user_id):
    form=BoardForm()
    if form.validate_on_submit():
        user=Board(
            title=form.title.data,
            content=form.content.data,
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.users"))
    return render_template("auth/create.html",form=form)