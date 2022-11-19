from fastapi import APIRouter
from .helper import receive_message

router = APIRouter()


@router.get('/poll-message/')
def poll_message():
    res = receive_message()
    if len(res):
        return res
    return {'message': 'No data found in Queue to poll'}
