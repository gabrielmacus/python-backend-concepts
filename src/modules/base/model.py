import datetime

class BaseModel:
    id:int = None
    created_at:datetime.datetime = None
    updated_at:datetime.datetime = None