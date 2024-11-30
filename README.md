# BookMyShow Online Ticket Booking Stream Data Processing-Project

This project demonstrates a real-time data processing pipeline for an online ticketing system using Azure services. It integrates **Event Hub**, **Stream Analytics**, and **Synapse Analytics** to process booking and payment data streams efficiently.

## **Project Overview**

The goal of this project is to:
1. Simulate real-time **booking** and **payment** events using Azure **Event Hub**.
2. Perform **real-time data transformation and window-based joins** with **Stream Analytics**.
3. Store the processed and enriched data in an **Azure Synapse Analytics** table for analysis.

## **Tech Stack**
- **Programming Language**: Python
- **Azure Services**:
  - **Event Hub**: Ingests booking and payment events.
  - **Stream Analytics Job**: Processes and joins streams in real-time.
  - **Synapse Analytics**: Stores processed data for analysis.
- **SQL**: For querying the Synapse table.

## **Project Flow**
1. **Mock Data Generation**:
   - Use Python to publish mock **booking** and **payment** data to Azure **Event Hubs**.

2. **Stream Processing**:
   - Use **Azure Stream Analytics** to:
     - Transform incoming data streams.
     - Perform window-based joins on bookings and payments occurring within **2 minutes** of each other.

3. **Data Storage**:
   - Write the processed data into **Azure Synapse Analytics** for further querying and reporting.

### **Prerequisites**
1. An active Azure account.
4. Python installed locally.

## Setup Instructions
1. **Create Azure Event Hub**:
   - Set up two Event Hubs: `Bookings` and `Payments`.
   - Add connection strings in `event_hub name: *** and event_hub_connection_primary_string : **** in python code by yourself where you create a Shared access policy to each event hub (topic) and their you can see connection string `.

2. **Publish Mock Data**:
   - Run `mock_booings.py` to send events to Event Hubs.
   - Run `mock_payments.py` to send events to Event Hubs.

3. **Set Up Azure Stream Analytics**:
   - Use `stream_analytics_job_query.sql` for the query.
   - Configure inputs (Event Hubs) and output (Synapse).

4. **Configure Azure Synapse**:
   - Create tables using `synapse_create_table.sql`.

5. **Test and Analyze**:
   - Verify the data using `synapse_create_table.sql  under   SQL:  SELECT * FROM BookingPayments WHERE event_category = 'Concert'; `.

## **What I Learned**
1. **Real-Time Streaming**:
   - Hands-on experience with ingesting and processing real-time data streams.
   - Using **Event Hub** for scalable data ingestion.

2. **Stream Analytics**:
   - Applying window-based operations and SQL-like transformations in **Azure Stream Analytics**.

3. **Data Warehousing**:
   - Storing and analyzing enriched data in **Azure Synapse Analytics**.
   - Writing complex queries to derive insights.

4. **End-to-End Data Engineering**:
   - Understanding the integration of Azure services to build a robust streaming data pipeline.

## **Conclusion and Importance**

- **Real-Time Insights**:
  This pipeline allows organizations to process and analyze booking and payment events in near real-time, ensuring better customer experience and operational efficiency.

- **Scalability**:
  Using **Event Hub** ensures that the system can handle a high volume of concurrent events without performance degradation.

- **Data Integration**:
  By combining bookings and payments data streams, businesses can gain enriched insights, such as analyzing customer behavior and improving fraud detection.
