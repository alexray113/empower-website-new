"""
A server file for Karl & Trey's gay little website 
"""
from flask import Flask, render_template, redirect, request, flash, session
import jinja2
import json

app = Flask(__name__)
app.secret_key = 's0m3TH!ng'

app.jinja_env.undefined = jinja2.StrictUndefined

app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

@app.route("/")
def view_homepage():

    return render_template("index.html")

@app.route("/services")
def view_services():

    return render_template("services.html")

@app.route("/contact/<name>", methods=["GET", "POST"])
def view_contact(name):
        
    if request.method == 'GET':
        name_check = name
        staffRoster = {}
        with open('EMPOWERSTAFFROSTER.json', 'r') as f:
            staffRoster = json.load(f)
            f.close()

        therapistInfo = {}
        for i, therapist in enumerate(staffRoster['data']):
            if therapist.get('name') == name_check:
                therapistInfo = staffRoster['data'][i]

        print(f'********therapist info! ::: {therapistInfo}')
            
        if therapistInfo == {}:
            return render_template("error.html")
        else:
            return render_template("contact-template.html", therapistInfo=therapistInfo)

    else:
        return render_template("error.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
