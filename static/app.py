# import necessary libraries
import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

client = pymongo.MongoClient()
db = client.mission_to_mars
collection = db.mars_data


#  create route that renders index.html template
@app.route("/")
def home():
    mars = list(db.mars_data.find())
    print(mars)
    return render_template("index.html", mars = mars)


@app.route("/scrape")
def scrape():
    mars = scrape_mars.scrape()
    db.mars_data.insert_one(mars)
    return "Some scraped data"

if __name__ == "__main__":
    app.run(debug=True)