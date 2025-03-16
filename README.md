# sales_data_project
Sales Data Analysis Project

## Introduction
This project involves the exploration and analysis of sales data using Python and various data science techniques. 
The goal is to clean, process, and analyze sales data, perform exploratory data analysis (EDA), and gain insights that can help improve decision-making. 
The project also includes data visualization and may involve saving the data to a database (SQL) for further analysis.

## Technology Used
1. Programming Language - Python
2. Scripting Language - SQL

## Data Set Used
A simple set of sales data from various regions and products. The dataset is used for performing data analysis and building machine learning models.
Here is the dataset used in the project: [Dataset Link](sample-sales-data.csv)]

**Original Data Source**: [sample-sales-data](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)

## Data Model
[Data Model_Sales_Distribution Image](Sales_Distribution.png)

## Scripts for Project
1. api_server.py: Handles API server setup, CSV upload, data processing, and SQL Server integration. [link](api_server.py)
2. data_import.py: Downloads the dataset from Kaggle and stores it in SQL Server. [link](data_import.py)
3. data_preprocessing.py: Cleans the data by removing duplicates and handling missing values. [link](data_preprocessing.py)
4. eda_sales_data.py: Performs exploratory data analysis (EDA) to visualize the data and analyze trends. [link](eda_sales_data.py)
5. table_creatae.sql: Ensures data integrity by checking for duplicates and missing values. [link](table_create.sql)

