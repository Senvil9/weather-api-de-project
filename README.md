# weather-api-de-project

## End-to-End Data pipeline from API to Dashboard
<img width="1132" height="334" alt="image" src="https://github.com/user-attachments/assets/82c8daa1-e903-49d2-a147-64834030afc6" />

This project demostrates a fully automated, containerized data pipeline that extracts, transforms, and visualizes live weather data in neal real-time. The architecture is designed to run entirely on an external server layer using **Docker**, ensuring that no tools are installed directly on the host operating system.

## Project Architecture

The data flow follows a modern data stack pattern:
1. **Extract** : A Python script retrieves weather data from the Weatherstack API.
2. **Orchestrate** : Apache Airflow schedules and manages the data ingestion tasks.
3. **Load** : Raw data is stored in a PostgreSQL database.
4. **Transform** : dbt (Data Build Tool) cleans and models the raw data into analytics-ready tables (staging and marts).
5. **Visualize** : Apache Superset connects to Postgres to display weather trends (e.g., temperature and wind speed) via interactive dashboards.

## Key Features
1. **Data Deduplication**: dbt models include logic to remove duplicate weather records based on timeframes.
2. **Automated Scheduling**: Airflow DAGs are configured to ingest data and trigger dbt transformations every 1 to 5 minutes.
3. **Persistent Storage**: Docker volumes ensure that database records and configurations persist even if the containers are stopped or removed.
4. **Production-Ready Vision**: The setup is designed for portability, allowing it to be easily moved to a production server.
