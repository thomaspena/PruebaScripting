# importar librerias
import requests # Biblioteca para realizar solicitudes HTTP de manera sencilla.
import json # Biblioteca para manejar datos en formato JSON

# Configuración de variables
url_del_servidor = "https://www.exampless.com/"  # Cambia esto por la URL del servidor que deseas comprobar
codigo_estado_esperado = 200  # Código de estado HTTP esperado
clave_api_sendgrid = "XXXXXXXXXXX" # API key de sendgrid
correo_destinatario = "XXXXXXX@XXXXXX.com"  # Correo del destinatario
correo_remitente = "XXXXXXXX@XXXXX.com"  # Correo del remitente
asunto_correo = "Alerta: El servidor web no responde correctamente"
cuerpo_correo = f"El servidor web {url_del_servidor} no está respondiendo correctamente. Código de estado esperado: {codigo_estado_esperado}."

# Función para enviar correo
def enviar_correo(asunto, cuerpo):
    datos_correo = {
        "personalizations": [
            {
                "to": [{"email": correo_destinatario}],
                "subject": asunto
            }
        ],
        "from": {"email": correo_remitente},
        "content": [
            {
                "type": "text/plain",
                "value": cuerpo
            }
        ]
    }

    encabezados = {
        "Authorization": f"Bearer {clave_api_sendgrid}",
        "Content-Type": "application/json"
    }

    respuesta = requests.post("https://api.sendgrid.com/v3/mail/send", headers=encabezados, data=json.dumps(datos_correo))
    
    # Imprimir la respuesta para verificar si se envió correctamente
    print("Código de estado de SendGrid:", respuesta.status_code)
    print("Respuesta de SendGrid:", respuesta.text)

# Comprobación del estado del servidor
try:
    respuesta_servidor = requests.get(url_del_servidor)
    codigo_estado_servidor = respuesta_servidor.status_code
    print(f"Código de estado del servidor: {codigo_estado_servidor}")

    if codigo_estado_servidor != codigo_estado_esperado:
        enviar_correo(asunto_correo, cuerpo_correo)
except requests.exceptions.RequestException as e:
    print("Error al conectar con el servidor:", e)
    # Enviar correo con un mensaje genérico
    mensaje_error_generico = f"No se pudo conectar al servidor {url_del_servidor}. Por favor, verifica la URL o el estado del servidor."
    enviar_correo(asunto_correo, mensaje_error_generico)

