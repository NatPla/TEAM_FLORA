from flask import Flask, render_template, request
from send_message import send_message

app = Flask("Email sender")

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
  form_data = request.form
  print form_data 

  send_message(form_data["email"], form_data["password"])

  return render_template("page1.html", email=form_data["email"])

@app.route("/search", methods=["POST"])

app.run()