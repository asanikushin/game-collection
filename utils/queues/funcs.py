import pika
from pika.exceptions import AMQPConnectionError

import socket
import time


def wait_connection(host: str, logger, wait_rounds: int = 10) -> pika.BlockingConnection:
    iteration = 0
    cur_sleep = 1
    sum_sleep = 0
    sleep_factor = 2

    connection = None
    while iteration < wait_rounds:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
            break
        except (AMQPConnectionError, socket.gaierror) as ex:
            if type(ex) == socket.gaierror:
                logger.warning(f"Problems with sockets: {ex.strerror}")
            else:
                logger.warning(f"Problems with AMPQ: {ex}")
            logger.info(f"Sleep for {cur_sleep} seconds")
            time.sleep(cur_sleep)
            sum_sleep += cur_sleep
            cur_sleep *= sleep_factor
        iteration += 1
        connection = None
    logger.info(f"Total sleep time {sum_sleep}")
    if connection is None:
        raise TimeoutError(f"Cannot create connection with RabbitMQ {host} for {wait_rounds} rounds and "
                           f"{sum_sleep} summary waiting time")
    return connection


def send_message(connection: pika.BlockingConnection, queue: str, message):
    channel = connection.channel()

    channel.queue_declare(queue=queue, durable=True)

    # TODO: add queue exchange
    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    connection.close()
