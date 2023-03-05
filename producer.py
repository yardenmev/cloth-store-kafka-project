from confluent_kafka import Producer
import random
import time
product_type = ["shirt", "pants", "skirt"]
card_type = ["visa","masteercartd", "goodi"]

producer = Producer({'bootstrap.servers': 'localhost:9094'})
while True:
    random_type = random.choice(product_type)
    random_card_type = random.choice(card_type)
    random_price = random.randint(10,50)
    random_id = random.randint(1000,10000)
    random_string = f'purchase #{random_id}:{random_type} paid {random_price}$ with {random_card_type}'
    producer.produce('store',value=random_string.encode('utf-8'))
    time.sleep(0.5)

     