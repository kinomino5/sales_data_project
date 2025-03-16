
mkdir C:\Users\YourUsername\.kaggle
move C:\Users\YourUsername\Downloads\kaggle.json C:\Users\YourUsername\.kaggle\

kyanyoga/sample-sales-data

import kaggle

# Dataset name from Kaggle
dataset_name = "kyanyoga/sample-sales-data"

# Download dataset to the "data" directory
kaggle.api.dataset_download_files(dataset_name, path="data", unzip=True)

print("✅ Kaggle dataset downloaded successfully!")

import pandas as pd

# Load CSV file into a DataFrame
df = pd.read_csv("data/sample-sales-data.csv", encoding="ISO-8859-1")

# Show first few rows
print(df.head())

import pandas as pd
import pyodbc
from sqlalchemy import create_engine, types

# Define SQL Server connection string
DB_CONNECTION_STRING = "mssql+pyodbc://localhost\\SQLEXPRESS/MyDatabase?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"

# Load the CSV file (Ensure the file path is correct)
file_path = "C:\\python\\PythonProjects\\RandyProject\\data\\sample-sales-data.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Ensure ORDERDATE is in proper format
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")

# Define a SQLAlchemy engine
engine = create_engine(DB_CONNECTION_STRING, fast_executemany=True)

# Explicitly define column data types
dtype_mapping = {
    "ORDERDATE": types.Date,
    "REGION": types.NVARCHAR(50),
    "MANAGER": types.NVARCHAR(50),
    "SALESMAN": types.NVARCHAR(50),
    "PRODUCT": types.NVARCHAR(50),
    "UNITS": types.Integer,
    "UNITCOST": types.Float,
    "TOTAL": types.Float
}

# Save DataFrame to SQL Server
df.to_sql("SalesData", con=engine, if_exists="replace", index=False, dtype=dtype_mapping)

print("✅ Data saved to SQL Server successfully!")
