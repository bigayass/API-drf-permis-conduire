from config  import settings
import smtplib
from email.message import EmailMessage
from datetime import datetime


def send_email_msg(operation):

	msg = EmailMessage()
	msg['Subject'] = f"Bot Mac Operation : {operation}"
	msg['From'] = settings.env('EMAIL')
	msg['To'] = "yasserazelmad@gmail.com"

	
	body = f"Le Bot est lancé depuis un ordinateur Mac.\n\
			Pour une opération : {operation}. \n\
			à l'heure : {datetime.now().strftime('%H:%M')}"
	
	msg.add_alternative(f"""\
		<!DOCTYPE html>
		<html>
			<body>
				<p>{body}</p>			
			</body>
		</html>
	""", subtype='html')


	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

		smtp.login(settings.env('EMAIL'), settings.env('PASSWORD'))

		smtp.send_message(msg)



