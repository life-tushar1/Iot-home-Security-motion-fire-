from pyfcm import FCMNotification
from email_flame import email_flame
class flame:
    def start(self):
        #to send push notification to android phone
        push_service = FCMNotification(api_key="")

        em=email_flame()
# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
 #ur device id
        registration_id = ""
        message_title = "FIRE Warning"
        message_body = "FLAMES DETECTED CONTACTING THE FIRE DEP. IMMEDIATELY "
        result = push_service.notify_single_device(registration_id, message_title=message_title, message_body=message_body)
        em.email()
# Conditional topic messaging
        print result
