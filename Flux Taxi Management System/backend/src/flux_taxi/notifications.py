# backend/src/flux_taxi/notifications.py
import firebase_admin
from firebase_admin import messaging

def send_push_notification(token, title, message):
    notification = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=message,
        ),
        token=token,
    )
    response = messaging.send(notification)
    return response
