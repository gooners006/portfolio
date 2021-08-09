import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


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
        except:
            return "not saved to database"
    else:
        return "something is wrong"


def write_to_file(data):
    with open("./venv/database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open("./venv/database.csv", mode="a", newline="") as database_csv:
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
