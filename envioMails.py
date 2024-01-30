import data
from email.message import EmailMessage
import ssl
import smtplib
import imghdr

# Configuración de las credenciales y direcciones de correo electrónico
email_emisor = 'diegogaraycullas@gmail.com'
email_password = data.MAILER_SECRET_KEY
email_receptor = ['elizabethgalvansandoval@gmail.com', 'analuisacullas@gmail.com']

# Configuración del correo electrónico
asunto = 'Prueba de correo'
mensaje = """
    <h1>Hola mundo</h1>
    <p>Este es un mensaje de prueba</p>
    <p>Saludos</p>
"""

# Crea el objeto EmailMessage y establece los campos del correo electrónico
em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
# Agrega el contenido del correo electrónico como HTML
em.set_content(mensaje, subtype='html')


# Agrega un archivo adjunto al correo electrónico
# Abre el archivo de imagen en modo binario ('rb') y lee su contenido
with open('20210705_084041.jpg', 'rb') as file:
    file_data = file.read()
    # Utiliza la biblioteca imghdr para determinar el tipo de archivo de imagen
    file_type = imghdr.what(file.name)
    # Obtiene el nombre del archivo
    file_name = file.name

# Agrega el archivo de imagen como un adjunto al objeto EmailMessage
em.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

# Configuración del contexto SSL para la conexión segura
context = ssl.create_default_context()

# Inicio de la conexión SMTP con el servidor de Gmail
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # Inicio de sesión con el correo electrónico del remitente y su contraseñ
    smtp.login(email_emisor, email_password)
    # Envío del correo electrónico
    smtp.sendmail(email_emisor, email_receptor, em.as_string())
    print('Correo enviado')