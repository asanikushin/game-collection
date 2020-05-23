#!/usr/bin/env python
from loader import create_app, db
from loader.process_importer import process_message

from utils.queues.funcs import wait_connection

from flask_script import Manager, Shell
from flask_migrate import MigrateCommand

import threading


def make_shell_context():
    return dict(app=app, db=db)


def callback(ch, method, properties, body):
    app.logger.info(f"Message for file: {body}")
    process_message(body.decode("utf-8"), app)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def run_consuming():
    with app.app_context():
        connection = wait_connection(app.config["RABBITMQ"], app.logger)
        channel = connection.channel()
        channel.queue_declare(queue=app.config["QUEUE"], durable=True)
        channel.basic_consume(on_message_callback=callback, queue=app.config["QUEUE"])
        channel.start_consuming()


app = create_app()
manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    rabbit = threading.Thread(target=run_consuming)
    rabbit.setName("RabbitMQ consumer")
    rabbit.start()

    manager.run()
    rabbit.join()
