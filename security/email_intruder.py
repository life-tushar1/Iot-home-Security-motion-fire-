import smtplib
class email_intruder:
    def email(self):
        fromaddr = 'xyz@gmail.com'
        toaddrs  = 'abc@gmail.com'
        username = 'xyz@gmail.com'
        password = 'xxxx'
        header = 'To:' + toaddrs + '\n' + 'From: ' + fromaddr + '\n' + 'Subject:Motion detected by automated sensors \n'
        msg = header + '\n this is a auto generated message from Home Security \n A motion was detected please check the broadcaste video for conformation if everything is alright \n\n'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
