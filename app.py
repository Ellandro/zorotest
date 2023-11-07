from flask import Flask, render_template, url_for, request, redirect, session, flash

app = Flask(__name__)

@app.route('/')
def Connexion():
    return render_template("login.html")

@app.route('/accueil/')
def accueil():
    return render_template("accueil.html")
if __name__== '__main__':
    app.run(debug=True)m
