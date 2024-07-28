import pika
import os
import ssl


def get_connection():
    rabbitmq_url = os.getenv('RABBITMQ_URL')  # Actualiza para usar RABBITMQ_URL
    rabbitmq_user = os.getenv('RABBITMQ_USER')
    rabbitmq_password = os.getenv('RABBITMQ_PASSWORD')

    # Extraer host y puerto del endpoint
    parsed_url = pika.URLParameters(rabbitmq_url)

    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)

    # Configuración SSL/TLS para cliente
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = True
    ssl_context.verify_mode = ssl.CERT_REQUIRED

    ssl_options = pika.SSLOptions(ssl_context, parsed_url.host)

    parameters = pika.ConnectionParameters(
        host=parsed_url.host,
        port=parsed_url.port,
        virtual_host=parsed_url.virtual_host,
        credentials=credentials,
        ssl_options=ssl_options
    )
    return pika.BlockingConnection(parameters)


connection = get_connection()
channel = connection.channel()
