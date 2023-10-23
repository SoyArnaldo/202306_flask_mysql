from flask import Flask, render_template, redirect, request, url_for, flash

# App
from app import app

from app.models.user import User

import bcrypt

@app.route("/")
def home():
    users = User.get_all()
    return render_template("index.html", users = users)

@app.route("/register/", methods = ["POST"])
def register():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"]
	}
    
    User.insert(data)
    flash("Resgristrado con éxito", "success")
    return redirect(url_for("home"))


@app.route("/show/<int:id>/")
def show(id):
    print("====================>", id)
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template("register.html", users= user )

@app.route("/delete/<int:id>/")
def delete(id):
    print("====================>", id)
    data = {
        "id": id
    }
    User.delete(data)
    flash("Eliminado con éxito", "info")
    return redirect(url_for("home"))

@app.route("/update/<int:id>/")
def update(id):
    data = {
        "id": id
    }
    users = User.get_one(data)
    return render_template("update.html", users = users)

@app.route("/update/<int:id>/end/", methods = ["POST"])
def update_user(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"]
	}
    User.update(data)
    flash("Actualizado con éxito", "success")
    return redirect(url_for("home"))