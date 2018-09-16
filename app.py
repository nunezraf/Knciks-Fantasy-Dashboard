# Dependencies
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
import scrape_fantasy

# Flask setup
app = Flask(__name__)

# app = "mongodb://rc:C00k1eBaba@ds143245.mlab.com:43245/heroku_n5qzr3nx"
# # client = MongoClient("mongodb://localhost:27017")

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/nba_app"
mongo = PyMongo(app)

# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)

# db = client.nba_db
# db = client.heroku_n5qzr3nx

# collection = db.nba
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
def scrape():
    # Run scrapped functions
    basketball = scrape_fantasy.scrape_nba_fantasy()

    #store results into a dictionary


    for i, player in enummerate(players):
       player_dict[i] = player



    #insert nba_dict into openDatabase

    mongo.db.collection.insert_one(basketball)

    #Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
