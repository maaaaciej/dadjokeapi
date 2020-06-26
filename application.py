from flask import Flask, render_template, jsonify, request
import random

#TODO 
#Sette opp database

app = Flask(__name__)

jokes =['Today, my son asked "Can I have a book mark?" and I burst into tears. 11 years old and he still doesn\'t know my name is Brian!', '']


#TODO I "/"
#return et random element fra databasen

@app.route("/")
def index():
   return  jokes[0]

#TODO I "/api"
#opprett et api som sender et json-objekt med en random joke fra databasen


@app.route("/api")
def api():
   return "api"