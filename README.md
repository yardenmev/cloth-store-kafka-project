Kafka day1 summary –Ex

• Simulating clothes store
• Start with:
• 1 borker
• 1 topic
• 1 partition
• We will have:
• 1 Producer
• 1 database consumer
• 1 payment gateway consumer
• 1 warehouse consumer

Producer: sending events simulating clothes purchases
• Random type (shirt, pants, skirt..)
• Random payment card type (visa, masrercard…)
• Random amount
• Produce 1 event every second (use sleep)

Database Consumer: simulates writing to the database
• Reads next message
• Prints content to the screen
• Sleep for 3 seconds between event

• Simulating clothes store
• Payment gateway Consumer: simulates charging the card
• Reads next message
• Prints content to the screen
• Sleep for 1 second between events

• Simulating clothes store
• Warehouse API consumer:
• Simulates sending packing details to the warehouse
• Reads next message
• Prints content to the screen
• No sleep in this case
