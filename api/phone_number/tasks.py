import os
from celery import shared_task
import requests


@shared_task
def send_message(receptor, token):
    response = requests.post(
        'https://api.kavenegar.com/v1/{}/verify/lookup.json'.format(
            os.getenv('KAVE_API')
        ),
        data={
            'receptor': receptor,
            'token': token,
            'template': 'fekrino'
        }
    )
    return response.status_code
