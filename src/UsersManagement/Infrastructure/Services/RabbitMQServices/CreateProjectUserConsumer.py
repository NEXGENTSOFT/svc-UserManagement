from src.UsersManagement.Infrastructure.Configurations.RabbitMQConfig import get_connection
from src.UsersManagement.Infrastructure.Utilities.MessageConverter import MessageConverter
from src.UsersManagement.Infrastructure.Controllers.ProjectsUsersControllers.CreateProjectsUsersController import CreateProjectsUsersController
import pika
from time import sleep


class CreateProjectUserConsumer:
    def __init__(self, controller: CreateProjectsUsersController, app):
        conection = get_connection()
        self.channel = conection.channel()
        self.channel.queue_declare(queue='create_project_user.queue', durable=True)
        self.controller = controller
        self.app = app

    def callback(self, ch, method, properties, body):
        text = body.decode()
        try:
            with self.app.app_context():
                json = MessageConverter.text_to_json(text)
                self.controller.run(json)
        except ValueError as e:
            print(f"Error procesando mensaje: {e}")

    def start_consuming_queue_create_project_user(self):
        while True:
            try:
                self.channel.queue_declare(queue='create_project_user.queue', durable=True)
                self.channel.basic_consume(queue='create_project_user.queue',
                                      on_message_callback=self.callback, auto_ack=True)
                self.channel.start_consuming()
            except pika.exceptions.AMQPConnectionError as e:
                print(f"Connection error: {e}, retrying in 5 seconds...")
                sleep(5)
            except Exception as e:
                print(f"Unexpected error: {e}")
                sleep(5)

