import random
import uuid
from faker import Faker
from datetime import datetime

# Initialize Faker for generating random data
faker = Faker()

def generate_event():
    """Generate a synthetic but realistic music streaming event with some dirty data."""
    
    event = {
        "event_id": str(uuid.uuid4()),  
        "timestamp": random.choice([
            datetime.utcnow().isoformat(),  
            datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S"),  
            None  
        ]),
        "event_type": random.choice([
            "Play", "pause", "SKIP", "Like", "DISLIKE", "Rewind", "fast_forward", "", None 
        ]),
        "user": {
            "user_id": str(uuid.uuid4()) if random.random() > 0.05 else None, 
            "username": faker.user_name() if random.random() > 0.1 else "", 
            "account_type": random.choice(["free", "premium", "trial", "banned"]) if random.random() > 0.03 else None,  # 3% missing
            "location": {
                "country": faker.country() if random.random() > 0.1 else "unknown",  
                "city": faker.city() if random.random() > 0.1 else "" 
            },
            "device": {
                "type": random.choice(["mobile", "desktop", "tablet", "smart speaker", None]),  
                "os": random.choice(["iOS", "Android", "Windows", "Linux", "Mac", ""])  
            },
        },
        "song": {
            "song_id": str(uuid.uuid4()) if random.random() > 0.02 else None,  
            "title": faker.sentence(nb_words=2) if random.random() > 0.05 else faker.sentence(nb_words=2).replace(" ", ""),  # Some titles without spaces
            "artist": faker.name() if random.random() > 0.05 else "",  
            "duration_sec": random.choice([random.randint(120, 300), None])  
        },
        "interaction": {
            "liked": random.choice([True, False, None]), 
            "added_to_playlist": random.choice([True, False, None]),  
        }
    }
    
    return event

# Quick test to see generated event
if __name__ == "__main__":
    print(generate_event())
