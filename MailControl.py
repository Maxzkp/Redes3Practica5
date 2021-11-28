from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

names = ['Ready', 'Set', 'Go']

def sendMail(subject, content, to):
	msg = MIMEMultipart()

	password = '2017630191'
	msg['From'] = 'saulcabrera.zk@gmail.com'
	msg['To'] = to

	msg['Subject'] = subject

	msg.attach(MIMEText(content, 'plain'))
	
	msg.attach(MIMEText('\n\nEnviado por Saul Cabrera Perez', 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()