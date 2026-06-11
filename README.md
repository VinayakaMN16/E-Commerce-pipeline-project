# Building an E-Commerce Data Engineering Pipeline with Google Cloud Platform

In this project, an end-to-end **E-Commerce Data Engineering Pipeline** was built using **Python, Google Cloud Platform (GCP), BigQuery, and Apache Airflow**. The objective of the project is to process raw e-commerce sales data, transform it into a structured format, and generate business insights for analytics and reporting.

## Data Extraction with Python

The pipeline begins by extracting e-commerce datasets containing customer, order, product, payment, and seller information. **Python** and **Pandas** are used to read and process the raw CSV files.

## Data Cleaning and Transformation

The extracted data is validated and cleaned by checking for null values, duplicate records, and data quality issues. Multiple datasets are then joined together to create a centralized **Sales Fact Table** for analytics.

### Data Quality Checks Performed

- Null Value Analysis
- Duplicate Record Validation
- Data Profiling
- Data Cleaning
- Data Transformation

## Storing Data in Google Cloud Storage (GCS)

The transformed sales dataset is uploaded to **Google Cloud Storage (GCS)**, which acts as the cloud storage layer for the pipeline.

## Loading Data into BigQuery

The processed data is loaded from **Google Cloud Storage** into **BigQuery**, Google's serverless data warehouse. BigQuery enables high-performance SQL analytics on large datasets.

## Apache Airflow Workflow

An **Apache Airflow DAG** is designed to automate the ETL workflow. The DAG manages the Extract, Transform, and Load processes and ensures that tasks execute in the correct sequence.

### Airflow Workflow

```text
Extract Data
      ↓
Transform Data
      ↓
Load Data into BigQuery
