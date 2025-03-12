from fastapi import FastAPI
from generator import generate_event 
from kafka import KafkaProducer
import json
import random
app = FastAPI()
import time
import uvicorn
# end point for event data
@app.get("/event_single")
def get_event_single():
    """Returns a single synthetic event"""
    return generate_event()

# kafka configuration 

KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "events_stream"

#initialize kafka producer
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))


#generate event to snd to kafka

@app.get("/event")
def get_event():
    """Generate a synthetic event and send it to Kafka"""
    event = generate_event()
    producer.send(KAFKA_TOPIC, value=event)
    return {"status": "event sent", "event": event}

@app.get("/event_stream")
def start_stream():
    """Stream multiple events to Kafka (simulating real-time data)."""
    for _ in range(5):  # Stream 10 events
        event = generate_event()
        producer.send(KAFKA_TOPIC, value=event)
        #print(f"Sent event: {event}")  # Log to console
        time.sleep(random.uniform(0.5, 2))  # Simulated real-time delay
        producer.flush()
    return {"status": "streaming finished"}

@app.on_event("shutdown")
def shutdown_event():
    """Gracefully close the Kafka producer on shutdown."""
    producer.close()



if __name__ == "__main__":
      uvicorn.run("event_generator:app", host="0.0.0.0", port=8000, reload=True)
