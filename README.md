# BookMyShow Online Ticket Booking Stream Data Processing-Project

This project demonstrates a real-time streaming pipeline for processing booking and payment data for an online ticketing system using Azure services.

## Tech Stack
- Python
- Azure Event Hub
- Azure Stream Analytics
- Azure Synapse Analytics
- SQL

## Architecture

1.Mock Data Source → Event Hub (Bookings & Payments)
2.Event Hub → Stream Analytics Job (Real-time transformation and joining)
3.Stream Analytics Job → Azure Synapse Data Warehouse

Python(Data publish) ---- Azure EventHub topics ----- Azure stream analytics job(transformations)  --- Azure synapse analytics(Datawarehouse storage)         


## Setup Instructions
1. **Create Azure Event Hub**:
   - Set up two Event Hubs: `Bookings` and `Payments`.
   - Add connection strings in `event_hub/event_hub_config.json`.

2. **Publish Mock Data**:
   - Run `mock_booings.py` to send events to Event Hubs.
   - Run `mock_payments.py` to send events to Event Hubs.

3. **Set Up Azure Stream Analytics**:
   - Use `stream_analytics_job_query.sql` for the query.
   - Configure inputs (Event Hubs) and output (Synapse).

4. **Configure Azure Synapse**:
   - Create tables using `synapse_create_table.sql`.

5. **Test and Analyze**:
   - Verify the data using `synapse_create_table.sql`.
  
-Ensures that only bookings and payments made within 2 minutes of each other are included in the output..
-DATEDIFF(minute, b, p) calculates the difference (in minutes) between the booking_time from b and payment_time from p.
