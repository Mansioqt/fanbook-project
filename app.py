from flask import Flask, render_template, jsonify, request
from datetime import datetime
from pymongo import MongoClient

connection_string = 'mongodb+srv://test:sparta@cluster0.gjjdcem.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(connection_string)
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')