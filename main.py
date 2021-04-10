import json
from schemas import RequestModel
from fastapi import FastAPI, Request

JSON_FILE_NAME = 'ranks.json'

app = FastAPI()

@app.get('/ranks')
async def get_rank(req: Request):
    with open(JSON_FILE_NAME, 'r') as file:
        data = json.load(file)
    return data

@app.post('/ranks')
async def post_rank(req: RequestModel):
    cr = str(req.current_rank)
    hr = str(req.highest_rank)
    ts = str(req.time_stamp)

    data_dict = {"cr": cr, "hr": hr, "ts": ts}

    try:
        with open(JSON_FILE_NAME, 'w') as file:
            json.dump(data_dict, file)
        return "Success!"
    except:
        return "Failure"