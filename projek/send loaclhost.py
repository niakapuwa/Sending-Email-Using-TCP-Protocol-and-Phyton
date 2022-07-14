import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "nikenayukpw@gmail.com"
toaddr = "nindasyafa@gmail.com"
#password = input(str("Please enter your password : "))
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "BISMILLAH LULUS"
 
body = "mari kita lulus dari pens yang keren ini"
 
msg.attach(MIMEText(body, 'plain'))

# Lampiran, sesuaikan nama filename dengan nama di attachment
#filename = "832143.png"
#attachment = open("C:\\Users\\LENOVO\\Pictures\\Saved Pictures\\832143.png", "rb")
 
part = MIMEBase('application', 'octet-stream')
#part.set_payload((attachment).read())
#encoders.encode_base64(part)
#part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('192.168.43.161', 1025)
#server.starttls()
#server.login(fromaddr, password)
#print("Login succes")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("Email has been sent to ", toaddr)
server.quit()