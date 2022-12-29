from flask import Flask, render_template, request, redirect, url_for
import os
from postgres import Postgres
import psycopg2

app = Flask(__name__)
DATABASE_URL = os.environ['DATABASE_URL']
print(DATABASE_URL)



@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
