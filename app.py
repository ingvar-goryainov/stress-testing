import flask
import json
from sync_db import get_random_row, get_by_index, insert_row

from flask import request

import redis

from time import time
from math import log
from random import random

TTL = 5
BETA = 1

redis_client = redis.Redis(host='localhost', port=6379, db=0)

app = flask.Flask("python-web-perf")

pool = None

@app.route("/insert", methods=['POST'])
def insert():
    data = request.get_json()
    index, value = data['index'], data['value']

    insert_row(index, value)
    return json.dumps({"index": str(index).zfill(10), "value": value})

@app.route("/get_random")
def get_random():
    index, value = get_random_row()
    return json.dumps({"index": str(index).zfill(10), "value": value})

@app.route("/get/<int:index>")
def get(index):
    index, value = get_by_index(index)
    return json.dumps({"index": str(index).zfill(10), "value": value})

@app.route("/get-simple-cache/<int:index>")
def get_simple_cache(index):
    cache_value = redis_client.get(str(index))
    if cache_value is None:
        _, value = get_by_index(index)
        redis_client.set(str(index), value, TTL)
    else:
        value = cache_value.decode()

    return json.dumps({"index": str(index).zfill(10), "value": value})


@app.route("/get-probalistic-cache/<int:index>")
def get_probalistic_cache(index):
    cache_value = redis_client.get(str(index))

    if cache_value is not None:
        value, delta, expire = cache_value.decode().split("|")

        delta = float(delta)
        expire = float(expire)


    if cache_value is None or ((time() - delta * BETA * log(random())) >= expire):
        start = time()
        _, value = get_by_index(index)

        delta = time() - start

        expire = time() + TTL
        cache_value = f"{value}|{delta}|{expire}"

        redis_client.set(str(index), cache_value, TTL)

    return json.dumps({"index": str(index).zfill(10), "value": str(value)})