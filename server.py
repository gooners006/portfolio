import csv
import os
from flask import Flask, render_template, request, redirect, send_from_directory

app = Flask(__name__)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static/assets"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_pages(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thank_you.html")
        except Exception as e:
            return f"{e}"
    else:
        return "something is wrong"


def write_to_file(data):
    with open("./database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open("./database.csv", mode="a", newline="") as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database_csv,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([email, subject, message])
