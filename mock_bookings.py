from azure.eventhub import EventHubProducerClient, EventData
import json
import time
import random
from faker import Faker

fake = Faker()

# Initialize Event Hub client
event_hub_connection_str = 'Endpoint=sb://streamevnthub.servicebus.windows.net/;SharedAccessKeyName=bookingssaspolicy;SharedAccessKey=5AldD0qmIX+cYLu1v+FGjJB21ne0P3T3W+AEhLl0X1g=;EntityPath=bookings'
event_hub_name = 'bookings'

producer = EventHubProducerClient.from_connection_string(
    conn_str=event_hub_connection_str,
    eventhub_name=event_hub_name
)

order_id_counter = 2000

def generate_booking_data():
    global order_id_counter
    order_id = order_id_counter
    order_id_counter += 1
    return {
        "order_id": f"order_{order_id}", 
        "booking_time": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "customer": {
            "customer_id": f"cust{order_id}",
            "name": fake.name(),
            "email": fake.email()
        },
        "event_details": {
            "event_id": f"event{random.randint(1, 100)}",
            "event_name": random.choice(["Concert", "Play", "Movie"]),
            "event_location": fake.address(),
            "seats": [
                {"seat_number": f"{random.choice(['A', 'B', 'C'])}{random.randint(1, 10)}", "price": random.randint(50, 100)},
                {"seat_number": f"{random.choice(['A', 'B', 'C'])}{random.randint(1, 10)}", "price": random.randint(50, 100)}
            ]
        }
    }

while True:
    try:
        mock_data = generate_booking_data()
        event_data = json.dumps(mock_data)
        event = EventData(event_data)
        producer.send_batch([event], partition_key=str(mock_data["order_id"]))
        print("Booking Event Published - ", event_data)
        time.sleep(5)
    except Exception as e:
        print(f"Error sending data: {e}")

producer.close()
