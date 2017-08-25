from pyfcm import FCMNotification
from email_intruder import email_intruder
class intrution:
    def start(self):
        push_service = FCMNotification(api_key="")

        em=email_intruder()
# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

        registration_id = ""
        message_title = "Warning"
        message_body = "Intrution alert beware"
        result = push_service.notify_single_device(registration_id, message_title=message_title, message_body=message_body)
        em.email()
# Conditional topic messaging
        print result
