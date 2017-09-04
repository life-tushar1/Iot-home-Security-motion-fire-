from pyfcm import FCMNotification
from email_intruder import email_intruder
from file_uploader import file_uploader

class intrution:
    def notifi_again(self):
        push_service = FCMNotification(api_key="")#firebase api key
        em=email_intruder()
        rec_up=file_uploader()
        rec_up.backup()
        registration_id = ""#device id
        message_title = "Warning"
        message_body = "Intrution alert beware check ur drop box for recording"
        result = push_service.notify_single_device(registration_id, message_title=message_title, message_body=message_body)
        em.email()
# Conditional topic messaging
        print result


    def start(self):
        push_service = FCMNotification(api_key="")#fire base api key


        em=email_intruder()
        rec_up=file_uploader()
        rec_up.rec_upload()
# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

        registration_id = ""#device registration_id
        message_title = "Warning"
        message_body = "Intrution alert beware check ur drop box for recording"
        result = push_service.notify_single_device(registration_id, message_title=message_title, message_body=message_body)
        em.email()
# Conditional topic messaging
        print result
