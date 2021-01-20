# amqps://vnksjtog:Nl1D0Uhm9A1pp0tZOxslt1eG15MsT28P@lionfish.rmq.cloudamqp.com/vnksjtog

import pika

params = pika.URLParameters('amqps://vnksjtog:Nl1D0Uhm9A1pp0tZOxslt1eG15MsT28P@lionfish.rmq.cloudamqp.com/vnksjtog')
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')