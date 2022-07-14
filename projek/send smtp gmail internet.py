#library smtp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "nindasyafa@gmail.com" #emailpengirim
toaddr = "nikenayukpw@gmail.com" #emailpenerima
password = input(str("Please enter your password : ")) #menulis password dari gmail pengirim  agar dapat berkomunikasi
msg = MIMEMultipart() #subclas dari MIMEBASE untuk banyak isian
 
msg['From'] = fromaddr #email pengirim
msg['To'] = toaddr #email penerima
msg['Subject'] = "WISUDAAA" #subject email
 
body = "ini coba" #body email
 
msg.attach(MIMEText(body, 'plain')) #menyisipkan body email dengan tipe plain

#Lampiran, sesuaikan nama filename dengan nama di attachment
#filename = "832143.png"
#attachment = open("C:\\Users\\LENOVO\\Pictures\\Saved Pictures\\832143.png", "rb")
 
part = MIMEBase('application', 'octet-stream') #mengirimkan dalam bentuk octet stream di layer application
part.set_payload((attachment).read()) #menyisipkan lampiran
encoders.encode_base64(part) #melkaukan encoding pengiriman default base64
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
#msg.attach(part) #menyisipkan variabel part ke email
 
server = smtplib.SMTP(smtp.gmail.com, 587) #server yang digunakan
server.starttls() #menjalankan enkripsi tls agar pesan dapat terkirim dengan baik dan aman ke penerima
server.login(fromaddr, password) #login ke server
print("Login succes")
text = msg.as_string() #mengubah bentuk file menjadi tipe data  string
server.sendmail(fromaddr, toaddr, text) #mengirimkan email
print("Email has been sent to ", toaddr) #menampilkan notifikasi di pengirim jika pesan sudah diterima ke email penerima
server.quit() #keluar dari server