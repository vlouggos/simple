from flask import Flask, render_template, request, redirect, url_for
import os
from postgres import Postgres
import psycopg2
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

#DATABASE_URL = os.environ['DATABASE_URL']

##CONNECT TO DB
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
### Optional: But it will silence the deprecation warning in the console.
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#db = SQLAlchemy(app)
#
#db.create_all()
#
###CREATE TABLE
@app.route('/')
def home():
    ##READ ALL RECORDS
    #all_books = db.session.query(Book).all()
    return render_template("index.html")#, books=all_books#


#@app.route("/add", methods=["GET", "POST"])
#def add():
#    if request.method == "POST":
#       new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
#       db.session.add(new_book)
#       db.session.commit()
#       return redirect(url_for('home'))
#    return render_template("add.html")
#
#@app.route('/rating', methods=["GET", "POST"])
#def rating():
#        if request.method == "POST":
#            book_id = request.form["id"]
#            book_to_update = Book.query.get(book_id)
#            book_to_update.rating = request.form["rating"]
#            db.session.commit()
#            return redirect(url_for('home'))
#        book_id = request.args.get('id')
#        book_selected = Book.query.get(book_id)
#        return render_template("rating.html", book=book_selected)
#
#@app.route('/delete')
#def delete():
#        book_id = request.args.get('id')
#        book_to_delete = Book.query.get(book_id)
#        db.session.delete(book_to_delete)
#        db.session.commit()
#        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
