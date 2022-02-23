from fastapi import FastAPI
import json
import re
import copy
app = FastAPI()

import redis

r = redis.Redis(
    host='localhost',
    port=6379)

@app.get("/pythonjobs")
def read_item(location: str, page:int):
    json_data = [obj for obj in json.loads(r.get(r'page-'+str(page))) if location in obj['Location']]
    return json_data
