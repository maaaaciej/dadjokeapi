from flask import Flask, render_template, jsonify, request
import random
from database import jokes

app = Flask(__name__)


#TODO 
#Lag en template som viser en random quote, med en knapp som refresher for å gi deg en ny en


@app.route("/")
def index():
   return  render_template("index.html", joke=random.choice(jokes))
   

#TODO I "/api"
#Lag en template som forklarer hvordan API'en fungerer, og CTA med å følge meg på github osv 

@app.route("/api")
def api():
   return " Hvordan api fungerer"


@app.route("/api/joke") 
def joke():
      return  jsonify(random.choice(jokes))
