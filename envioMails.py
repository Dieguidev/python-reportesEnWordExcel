import data
from email.message import EmailMessage
import ssl
import smtplib

email_emisor = 'diegogaraycullas@gmail.com'
email_password = data.MAILER_SECRET_KEY
email_receptor = 'diegogaraycullas@gmail.com'

asunto = 'Prueba de correo'

mensaje = """
    <h1>Hola mundo</h1>
    <p>Este es un mensaje de prueba</p>
    <p>Saludos</p>
"""

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(mensaje, subtype='html')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_emisor, email_password)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())
    print('Correo enviado')