import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'digi_meals'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipe.html", recipes=mongo.db.recipe.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
    categories=mongo.db.categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

@app.route('/add_carousel')
def add_carousel():
    return render_template("carousel.html",
    utensils=mongo.db.utensils.find())



if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)