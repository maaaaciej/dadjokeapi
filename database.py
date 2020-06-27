#inserting python list into database
import csv
import os




#TODO
#program that imports a txt or csv list of jokes
#convert txt or csv file to a python list

f=open("jokes.txt")
jokes = f.readlines()

for joke in jokes:
    print(joke)