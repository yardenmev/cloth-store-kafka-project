from confluent_kafka import Consumer
import time

consumer = Consumer({'bootstrap.servers': 'localhost:9094','group.id': 'warehouse','auto.offset.reset': 'earliest'})
consumer.subscribe(['store'])

while True:
    msg = consumer.poll()
    print(f"Sending request to the warehouse: {msg.value().decode('utf-8')}")
    # consumer.close()

