#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#import sys
from flask import Flask, render_template
from wrappers.osc import MididingsOsc

app = Flask(__name__)

osc = MididingsOsc()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/mididings/<command>/", defaults={'value': None}, strict_slashes=False)
@app.route("/mididings/<command>/<int:value>")
def mididings(command, value=None):
    osc.send_message('/' + command, value)
    return ('', 204)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
