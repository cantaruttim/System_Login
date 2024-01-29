from flask import render_template, url_for, redirect
from Homepage import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from Homepage.forms import FormLogin, FormCreateAccount
from Homepage.models import User


@app.route("/", methods=["GET", "POST"])
def login():
    formlogin = FormLogin()

    if formlogin.validate_on_submit():
        user = User.query.filter_by(email=formlogin.email.data).first()
        if user and bcrypt.check_password_hash(user.password, formlogin.password.data):
            login_user(user)
            return redirect(url_for("perfil", id=user.id))
    return render_template('login.html', form=formlogin)


@app.route("/create-account", methods=["GET", "POST"])
def create_account():
    form_createaccount = FormCreateAccount()

    if form_createaccount.validate_on_submit():
        password = bcrypt.generate_password_hash(form_createaccount.password.data)
        user = User(email=form_createaccount.email.data,
                             username=form_createaccount.username.data,password=password)

        database.session.add(user)
        database.session.commit()

        login_user(user, remember=True)

        return redirect(url_for("perfil", id=user.id))
    return render_template('create_account.html', form=form_createaccount)


@app.route("/perfil/<id>")
@login_required
def perfil(id):
    if int(id) == int(current_user.id):
        # own perfil
        return render_template('perfil.html', user=current_user)
    else:
        user = User.query.get(int(id))
        return render_template('perfil.html', user=user)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))