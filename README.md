# NYC MTA Predictive Insights

This directory contains the setup used for orchestrating the data pipelines within the NYC MTA Predictive Insights and Forecasting Dashboard project.

## Purpose

Airflow is used here to schedule, monitor, and manage the project's workflows, including:
* Data ingestion from sources (Kafka).
* Data processing and transformation (triggering Flink jobs or using Python operators).
* Model training and evaluation (using PyTorch, potentially managed by Ray and logged with MLFlow).
* Data loading into storage (Cassandra).
* Monitoring checks and alerts (Prometheus and Grafana).
