from fastapi import FastAPI, HTTPException
from typing import Optional

import controller

app = FastAPI()

@app.get("/pythonjobs")
def read_item(location: Optional[str] = None, page: Optional[int] = None):
    conn = controller.Controller()
    if location == None and page == None:
        return conn.getTop(10)
    elif location == None or page == None:
        raise HTTPException(status_code=422, detail="Please pass both Param location and Page parameters")
    else:
        return conn.getJobsInLocationAtPage(location, page)
