from flask import Flask, render_template, request
from send_message import send_message
from flowerdictionaryoption2 import size_dictionary, colour_dictionary, smell_dictionary, season_dictionary, latin_dictionary, maintenance_dictionary, find_feature, return_all_flower_features

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
def search():
  form_data = request.form # request.form is used to assign data passed in through search to form_data. In this case a flower is expected.
  flower_being_searched_for = form_data["flower"] # Find the desired flower enetry from form_data and assign it to flower_being_searched_for
  # Given the flower, we want to find all relevant information to said flower.
  flowers = find_feature(smell_dictionary,flower_being_searched_for)
  # Following depends on featurs being returned in right order. If any flower does not have an entry in one of the dictionaries, or multiple, things will go very wrong.
  #  The .HTML file is not set up to use these things, but these strings should be passed in to it from here.
  return render_template("flower.html", flower=flowers)

app.run()
