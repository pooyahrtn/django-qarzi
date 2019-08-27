from celery import shared_task
from firebase_admin import messaging


@shared_task
def send_notification(to_user_token, title, body, data={}):
    message = messaging.Message(
        data=data,
        notification=messaging.Notification(body=body, title=title),
        token=to_user_token,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)
