import smtplib
class email_flame:
    def email(self):
        fromaddr = 'xyz@gmail.com'
        toaddrs  = 'abc@gmail.com'
        username = 'xyz@gmail.com'
        password = 'xxxx'
        header = 'To:' + toaddrs + '\n' + 'From: ' + fromaddr + '\n' + 'Subject:flames detected by automated sensors \n'
        msg = header + '\n this is a auto generated message from Home Security \n A fire  was detected plz come immediately for fire extingushing to \n address- \n\n'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
