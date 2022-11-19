import json
from fastapi import APIRouter,HTTPException
from .helper import send_message
from .validations import Message

router = APIRouter()


@router.post('/add-message')
def add_message(message: Message):
    data = dict(message)
    response = send_message(json.dumps(data))
    print(response)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {'message':'Successfully Published to Queue'}
    raise HTTPException(status_code='404',detail=f'Error Occurred')
