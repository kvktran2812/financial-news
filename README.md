# Financial data pipeline  
## Overview  

This project demonstrates a financial data pipeline that collects, processes, and stores stock data from Yahoo Finance. The pipeline uses an ETL (Extract, Transform, Load) approach to ensure accurate and structured data, making it easy for analysis, reporting, and further data science applications. The primary focus is on creating a robust, scalable, and maintainable pipeline suitable for real-time financial data processing.  

## Project Structure  

The project is divided into the following core components:  
- Data Extraction: Data is fetched from Yahoo Finance's API, focusing on various stock data attributes such as prices, volume, and other financial indicators.
- Data Transformation: Extracted data is cleaned and transformed to ensure consistency and quality. Transformations include handling missing values, data type conversions, and feature engineering to create additional useful attributes.
- Data Loading: The processed data is stored in a database or a data warehouse. For this project, data can be loaded into PostgreSQL, AWS RDS, or any other compatible data warehouse solution for easy access and analysis.
- Automation: The entire pipeline is scheduled to run automatically at regular intervals, ensuring that the data is always up to date.

## Technologies Used  

- Python: Core programming language for scripting the ETL processes.
- Pandas: Used for data manipulation and transformation.
- Yahoo Finance API: For retrieving stock data.
- SQL Database: PostgreSQL or similar database for storing transformed data.
- Airflow: Task scheduler for managing and automating the ETL pipeline.
- Docker: Containerization to ensure consistency across environments.
