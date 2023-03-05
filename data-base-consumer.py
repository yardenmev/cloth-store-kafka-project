from confluent_kafka import Consumer
import time

consumer = Consumer({'bootstrap.servers': 'localhost:9094','group.id': 'DB','auto.offset.reset': 'earliest'})
consumer.subscribe(['store'])

while True:
    msg = consumer.poll()
    print(f"Saving to db: {msg.value().decode('utf-8')}")
    # consumer.close()
    time.sleep(3)
