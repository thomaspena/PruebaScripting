# Importacion de librerias
import requests
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Variables de configuración
URL_SERVIDOR = 'COLOCAR_URL_SERVIDOR'
SENDGRID_API_KEY = 'TU_SENDGRID_API_KEY'
CORREO_EMISOR = 'COLOCAR_CORREO_EMISOR'
CORREO_DESTINO = 'COLOCAR_CORREO_DESTINO'
ASUNTO = 'EL SERVIDOR NO RESPONDE'
# Función para verificar el estado del servidor
def estado_servidor(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f'Error al conectar con el servidor: {e}')
        return False

# Función para enviar correo
def enviar_email(api_key, correo_emisor, correo_destino, asunto, contenido):
    message = Mail(
        from_email=correo_emisor,
        to_emails=correo_destino,
        subject=asunto,
        html_content=contenido
    )
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(f'Correo enviado: {response.status_code}')
    except Exception as e:
        print(f'Error al enviar el correo: {e}')

# Función para ejecutar el script
def main():
    if not estado_servidor(URL_SERVIDOR):
        contenido = f'<strong>El servidor {URL_SERVIDOR} no está respondiendo correctamente.</strong>'
        enviar_email(SENDGRID_API_KEY, CORREO_EMISOR, CORREO_DESTINO, ASUNTO, contenido)
    else:
        print(f'El servidor {URL_SERVIDOR} está funcionando correctamente.')

if __name__ == '__main__':
    main()
