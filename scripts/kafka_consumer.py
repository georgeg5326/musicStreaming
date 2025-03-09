from kafka import KafkaConsumer
import json



# KAFAK configuration
KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "events_stream"

#initialize kafka consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("starting Kafka Consumer")

# consume messages fro kafka
for message in consumer:
    print("Consumed message", message.value)
