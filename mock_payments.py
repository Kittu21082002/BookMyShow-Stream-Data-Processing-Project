from azure.eventhub import EventHubProducerClient, EventData
import json
import time
import random
from faker import Faker

fake = Faker()

# Initialize Event Hub client
event_hub_connection_str = 'Endpoint=sb://streamevnthub.servicebus.windows.net/;SharedAccessKeyName=paymentssaspolicy;SharedAccessKey=JSnFUH9eI8JbIxfwaTaJIcKsiKGKoV3q/+AEhJLXnrU=;EntityPath=payments'
event_hub_name = 'payments'

producer = EventHubProducerClient.from_connection_string(
    conn_str=event_hub_connection_str,
    eventhub_name=event_hub_name
)

payment_id_counter = 3000
order_id_counter = 2000

def generate_payment_data():
    global payment_id_counter, order_id_counter
    payment_id = payment_id_counter
    order_id = order_id_counter
    payment_id_counter += 1
    order_id_counter += 1
    return {
        "payment_id": f"payment_{payment_id}", 
        "order_id": f"order_{order_id}", 
        "payment_time": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "amount": random.randint(100, 200),
        "payment_method": random.choice(["Credit Card", "Debit Card", "PayPal"]),
        "payment_status": random.choice(["Success", "Failed"])
    }

while True:
    try:
        mock_data = generate_payment_data()
        event_data = json.dumps(mock_data)
        event = EventData(event_data)
        producer.send_batch([event], partition_key=str(mock_data["order_id"]))
        print("Payment Event Published - ", event_data)
        time.sleep(5)
    except Exception as e:
        print(f"Error sending data: {e}")

producer.close()
