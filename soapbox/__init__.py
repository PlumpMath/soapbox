#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Flask
from flask import request
import requests
import os
app = Flask(__name__)

def send_simple_message(subject, body):
    # print("environ.getment: {}, {}, {}, {}".format(os.environ.get("MAILGUN_HOST"), os.environ.get("MAILGUN_KEY"), os.environ.get("MAILGUN_FROM"), os.environ.get("TUMBLR_EMAIL")))
    return requests.post(
        os.environ.get("MAILGUN_HOST"),
        auth=("api", os.environ.get("MAILGUN_KEY")),
        data={"from": os.environ.get("MAILGUN_FROM"),
              "to": os.environ.get("TUMBLR_EMAIL"),
              "subject": subject,
              "text": body})

@app.route("/")
def hello():
  return "Hi, this is the plusonenews publisher, and it's called SOAPBOX."

@app.route('/publish', methods=['POST'])
def publish():
    body = u''.join((request.form['body'])).encode('utf-8').strip()
    subject = u''.join((request.form['subject'])).encode('utf-8').strip()
    print("Publishing subject={}, body={}".format(subject, body))
    resp = send_simple_message(subject=subject, body=body)
    return "{} OK".format(resp.status_code)

