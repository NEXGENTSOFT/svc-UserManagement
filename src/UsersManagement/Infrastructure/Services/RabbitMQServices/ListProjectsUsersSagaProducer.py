import pika
from src.UsersManagement.Infrastructure.Configurations.RabbitMQConfig import get_connection
from src.UsersManagement.Infrastructure.Utilities.MessageConverter import MessageConverter

class ListProjectsUsersSagaProducer:

    def run(self, new_request):
        connection = get_connection()
        try:
            channel = connection.channel()
            channel.queue_declare(queue='list_project_user_requester.queue', durable=True)
            channel.queue_declare(queue='list_project_user_responser.queue', durable=True)

            message_converter = MessageConverter()

            correlation_id = new_request.get('session_uuid')
            payload = message_converter.json_to_text(new_request)

            channel.basic_publish(
                exchange='',
                routing_key='list_project_user_requester.queue',
                body=payload,
                properties=pika.BasicProperties(
                    delivery_mode=2,
                    correlation_id=correlation_id
                )
            )

            self.response = None

            def on_response(ch, method, props, body):
                if props.correlation_id == correlation_id:
                    self.response = message_converter.text_to_json(body)

            channel.basic_consume(
                queue='list_project_user_responser.queue',
                on_message_callback=on_response,
                auto_ack=True
            )

            while self.response is None:
                connection.process_data_events(time_limit=1)  # Ajusta el tiempo de espera según sea necesario

        finally:
            channel.close()
            connection.close()

        return self.response
