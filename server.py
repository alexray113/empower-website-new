"""
A server file for Karl & Trey's gay little website 
"""
from flask import Flask, render_template, redirect, request, flash, session
import jinja2

app = Flask(__name__)
app.secret_key = 's0m3TH!ng'

app.jinja_env.undefined = jinja2.StrictUndefined

app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

@app.route("/")
def view_homepage():

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
