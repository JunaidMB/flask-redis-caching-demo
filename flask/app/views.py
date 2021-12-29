from app import app 
from flask import render_template, request, redirect, jsonify, make_response, send_from_directory, abort, flash, url_for, session
from datetime import datetime
import os
import redis
import time as t
import ast
from werkzeug.utils import secure_filename

# Connect to Redis instance
r = redis.Redis(host="redis.default.svc.cluster.local", port=6379)

users = {
'Bob': {"Age": "31", "Occupation": "Data Engineer", "Favourite Food": "Spagetti"},
'Alice': {"Age": "24", "Occupation": "Software Engineer", "Favourite Food": "Tuna"},
'James': {"Age": "27", "Occupation": "Devops Engineer", "Favourite Food": "Pizza"},
'Farida': {"Age": "19", "Occupation": "Intern", "Favourite Food": "Vegan Steak"}
}

@app.route("/", methods= ['GET'])
def get_user():

    user = request.args.get("user")

    if r.exists(user):
        print("Fetching from Redis")
        record = ast.literal_eval(r.get(user).decode("utf-8"))
    else:
        if user in users.keys():
            print('Simulating a 5 second delay')
            t.sleep(5)
            record = users[user]
            r.set(user, str(record), ex=3)
        else:
            record = "User Not Found"

    return record