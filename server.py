import requests
from flask import Flask, render_template, request
import smtplib
import os


OWN_EMAIL = os.environ["OWN_EMAIL"]
OWN_PASSWORD = os.environ["OWN_PASSWORD"]

app = Flask("__name__")
print(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        send_email(name, email, message)
        return render_template("go.html")


def send_email(name, email, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(
            from_addr=OWN_EMAIL,
            to_addrs=OWN_EMAIL,
            msg=f"subject:WEBSITE VISITED\n\nhay parth some one has reached your site here are the credentials of the person\n name - {name}\n email - {email}\n message is - {message}"
        )


if __name__ == "__main__":
    app.run(debug=True)
