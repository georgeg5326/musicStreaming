from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "events_stream"

admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_BROKER)

# Define topic configuration
topic_list = [NewTopic(name=TOPIC_NAME, num_partitions=3, replication_factor=1)]

try:
    admin_client.create_topics(new_topics=topic_list, validate_only=False)
    print(f"Topic '{TOPIC_NAME}' created successfully.")
except TopicAlreadyExistsError:
    print(f"Topic '{TOPIC_NAME}' already exists.")

admin_client.close()
