from flask import Flask, render_template, url_for, redirect, request
import requests
app = Flask(__name__)


@app.route("/")
def show_welcome():
    return render_template("welcome.html")


@app.route("/registration")
def show_registration():
    return render_template("reg_page.html")


@app.route("/index")
def show_table():
    response = requests.get('https://swapi.co/api/planets/?page=1').json()
    content = response['results']
    return render_template("index.html", table=content)


@app.route("/index/1")
def show_table1():
    response = requests.get('https://swapi.co/api/planets/?page=2').json()
    content = response['results']
    return render_template("index.html", table=content)


@app.route("/index/2")
def show_table2():
    response = requests.get('https://swapi.co/api/planets/?page=3').json()
    content = response['results']
    return render_template("index.html", table=content)


if __name__ == '__main__':
    app.run(debug=True)
