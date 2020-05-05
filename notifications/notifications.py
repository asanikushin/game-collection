#!/usr/bin/env python3

from notifications import BaseConfig, send_email

from utils.queues import Email, wait_connection

import pika

import logging
import pickle
import socket


def callback(ch, method, properties, body):
    logging.debug(" [x] Received %r" % (body,))
    logging.info(" [x] Received")
    data: Email = pickle.loads(body)
    try:
        send_email(address=data.email, message=data.message, subject=data.subject)
    except socket.gaierror:
        logging.error(" [o] Error while sending email")
        return

    logging.info(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


logging.basicConfig(
    format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logging.info(__name__)
logging.info("Start connecting")
connection: pika.connection = wait_connection(BaseConfig.RABBITMQ, logging)

logging.info(BaseConfig.QUEUE)
channel = connection.channel()
channel.queue_declare(queue=BaseConfig.QUEUE, durable=True)

logging.info(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_consume(on_message_callback=callback, queue=BaseConfig.QUEUE)

channel.start_consuming()
