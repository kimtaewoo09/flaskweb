from flask import Flask, Blueprint, render_template, redirect, url_for
from apps.app import db
from apps.auth.models import User_auth
from apps.auth.forms import UserForm

auth=Blueprint(
    "auth", __name__,
    template_folder="template",
    static_folder="static"
)
@auth.route("/")
def index():
    return render_template("auth/test.html")
@auth.route('/users')
def users():
    users=User_auth.query.all()
    return render_template('auth/test.html', users=users)
@auth.route('/users/new',methods=["GET","POST"])
def create_user():
    form=UserForm()
    if form.validate_on_submit():
        user=User_auth(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            number=form.number.data
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.users"))
    return render_template("auth/create.html",form=form)
@auth.route('/user/<user_id>',methods=["GET","POST"])
def edit_user(user_id):
    form=UserForm()
    user=User_auth.query.filter_by(id=user_id).first()
    print('!!!!!!!!!',user)
    if form.validate_on_submit():
        
        user.username=form.username.data
        user.email=form.email.data
        user.password=form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.users'))
    return render_template('auth/edit.html',user=user, form=form)
@auth.route('/user/<user_id>/delete',methods=["POST"])
def delete_user(user_id):
    user=User_auth.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('auth.users'))
