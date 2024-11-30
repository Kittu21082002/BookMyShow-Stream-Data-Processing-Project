# BookMyShow Online Ticket Booking Stream Data Processing-Project

This project demonstrates a real-time streaming pipeline for processing booking and payment data for an online ticketing system using Azure services.

## Tech Stack
- Python
- Azure Event Hub
- Azure Stream Analytics
- Azure Synapse Analytics
- SQL

## Architecture


## Setup Instructions
1. **Create Azure Event Hub**:
   - Set up two Event Hubs: `Bookings` and `Payments`.
   - Add connection strings in `event_hub/event_hub_config.json`.

2. **Publish Mock Data**:
   - Run `mock_data_publisher.py` to send events to Event Hubs.

3. **Set Up Azure Stream Analytics**:
   - Use `stream_analytics_query.sql` for the query.
   - Configure inputs (Event Hubs) and output (Synapse).

4. **Configure Azure Synapse**:
   - Create tables using `synapse_table_creation.sql`.

5. **Test and Analyze**:
   - Verify the data using `sample_queries.sql`.
