from flask import Flask, render_template, request, redirect, url_for
#import os
#from postgres import Postgres
#import psycopg2
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
#
##CONNECT TO DB
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
### Optional: But it will silence the deprecation warning in the console.
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#db = SQLAlchemy(app)
#
###CREATE TABLE
#class Book(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    title = db.Column(db.String(250), unique=True, nullable=False)
#    author = db.Column(db.String(250), nullable=False)
#    rating = db.Column(db.Float, nullable=False)
#
#    # Optional: this will allow each book object to be identified by its title when printed.
#    def __repr__(self):
#        return f'<Book {self.title}>'
#
#db.create_all()


@app.route('/')
def home():
    #new_book = Book(title="title1", author="author1", rating=10)
    #db.session.add(new_book)
    #db.session.commit()
    #book_to_print = Book.title
    return render_template("index.html", alpha="book_to_print")

if __name__ == "__main__":
    app.run(debug=True)
