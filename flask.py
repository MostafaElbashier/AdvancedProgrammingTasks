#!/usr/bin/env python3

from flask import Flask, render_template_string, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "change_this_in_production"

template_main = """
<!doctype html>
<html>
  <head>
    <style>
        body {
          font-family: Arial, sans-serif;
          max-width: 350px;
          margin: 40px auto;
          text-align: center;
        }
        input {
          width: 100%;
          padding: 8px;
          margin: 6px 0;
        }
        button {
          padding: 8px 15px;
          cursor: pointer;
        }
    </style>
    <title>{{ view.title() }}</title>
  </head>
  <body>
    <h2>{{ view.title() }}</h2>
    <form method="POST">
      <input type="text" name="uid" placeholder="User ID" required /><br />
      <input type="password" name="pwd" placeholder="Password" required /><br />
      <button type="submit">
        {% if view == 'enter' %}Enter{% else %}Register{% endif %}
      </button>
    </form>
    <p>
      {% if view == 'enter' %}
        New? <a href="/new">Register</a>
      {% else %}
        Have account? <a href="/enter">Enter</a>
      {% endif %}
    </p>
  </body>
</html>
"""

template_home = """
<!doctype html>
<html>
  <head>
    <style>
        body {
          font-family: Arial, sans-serif;
          max-width: 350px;
          margin: 40px auto;
          text-align: center;
        }
    </style>
    <title>Home</title>
  </head>
  <body>
    <h2>Hello, {{ current }}</h2>
    <a href="/exit">Leave</a>
  </body>
</html>
"""

def start_db():
    db = sqlite3.connect("app.db")
    c = db.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS accounts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uid TEXT UNIQUE,
            pwd TEXT
        );
        """
    )
    db.commit()
    db.close()

@app.route("/")
def index():
    if "current" in session:
        return render_template_string(template_home, current=session["current"])
    return redirect(url_for("enter"))

@app.route("/new", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uid = request.form.get("uid")
        pwd = request.form.get("pwd")

        db = sqlite3.connect("app.db")
        c = db.cursor()

        try:
            c.execute(
                "INSERT INTO accounts (uid, pwd) VALUES (?, ?)",
                (uid, pwd),
            )
            db.commit()
            db.close()
            return redirect(url_for("enter"))
        except sqlite3.IntegrityError:
            db.close()
            return """
            <p>ID taken.</p>
            <p><a href="/new">Back</a></p>
            """
    return render_template_string(template_main, view="register")

@app.route("/enter", methods=["GET", "POST"])
def enter():
    if request.method == "POST":
        uid = request.form.get("uid")
        pwd = request.form.get("pwd")

        db = sqlite3.connect("app.db")
        c = db.cursor()
        c.execute(
            "SELECT * FROM accounts WHERE uid=? AND pwd=?", (uid, pwd)
        )
        user = c.fetchone()
        db.close()

        if user:
            session["current"] = uid
            return redirect(url_for("index"))

        return """
        <p>Wrong ID or password.</p>
        <p><a href="/enter">Back</a></p>
        """
    return render_template_string(template_main, view="enter")

@app.route("/exit")
def exit():
    session.pop("current", None)
    return redirect(url_for("enter"))

if __name__ == "__main__":
    start_db()
    app.run()
