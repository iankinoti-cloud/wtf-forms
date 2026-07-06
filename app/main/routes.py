from flask import render_template, flash, redirect, url_for, request
from app import db
from app.main import main
from app.main.forms import RegistrationForm
from app.models import User, Post


@main.route("/community")
def community():
    users = User.query.order_by(User.username).all()
    post_count = Post.query.count()
    return render_template("main/community.html", users=users, post_count=post_count)


@main.route("/")
def index():
    return redirect(url_for("main.register"))


@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    registered = False
    has_errors = False
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            form.username.errors.append("That username is already taken.")
            has_errors = True
        elif User.query.filter_by(email=form.email.data).first():
            form.email.errors.append("That email is already registered.")
            has_errors = True
        else:
            user = User(username=form.username.data, email=form.email.data)
            user.password = form.password.data  # hashed by the setter
            db.session.add(user)
            db.session.commit()
            flash(f"Account created for {user.username}!", "success")
            registered = True
            form = RegistrationForm(formdata=None)  # clear fields after success
    elif request.method == "POST":
        has_errors = True
    return render_template("main/register.html", form=form, registered=registered, has_errors=has_errors)
