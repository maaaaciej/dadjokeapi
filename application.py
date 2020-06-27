from flask import Flask, render_template, jsonify, request
import random
from database import jokes

app = Flask(__name__)


#TODO 
#Lag en template som viser en random quote, med en knapp som refresher for å gi deg en ny en


@app.route("/")
def index():
   return  random.choice(jokes)

#TODO I "/api"
#opprett et api som sender et json-objekt med en random joke fra databasen


@app.route("/api")
def api():
   return "api"