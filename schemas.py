from pydantic import BaseModel

class RequestModel(BaseModel):
    highest_rank: int
    current_rank: int
    time_stamp: str