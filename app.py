# Dependencies
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
import scrape_fantasy

# Flask setup
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/nba_app"
mongo = PyMongo(app)

#create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    #find data
    fantasy= mongo.db.fantasy.find_one()



     # nba = db.nba.find()
     # return template and data
    return render_template("index.html", fantasy=fantasy)

#route that will trigger scrape functions
@app.route('/scrape')
def index():
    # Run scrapped functions
    nba = scrape_fantasy.scrape_nba_fantasy()

    #store results into a dictionary

    mvp = {
        "news_title":nba["news_title"],
        "news_img":nba["news_img"],
        "players":nba["players"],
    }

    #insert nba_dict into openDatabase

    mongo.db.fantasy.collection.insert_one(mvp)

    #Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
