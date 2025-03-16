# 필요한 라이브러리 import
from fastapi import FastAPI, UploadFile, File
import pandas as pd
import pyodbc
import io
from sqlalchemy import create_engine, types
import os

# FastAPI 앱 생성
app = FastAPI()

# SQL Server 연결 정보
DB_CONNECTION_STRING = "mssql+pyodbc://localhost\\SQLEXPRESS/MyDatabase?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"

# CSV 파일 업로드 API
@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    try:
        # 업로드된 파일 읽기
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents), encoding='ISO-8859-1')

        # 데이터 확인 (첫 5행 출력)
        print(df.head())

        # 데이터가 비어있는지 확인
        if df.empty:
            return {"error": "The uploaded CSV file is empty!"}

        # ORDERDATE 열을 datetime 형식으로 변환
        df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

        # SQLAlchemy 엔진 생성
        engine = create_engine(DB_CONNECTION_STRING, fast_executemany=True)

        # 데이터 타입 지정
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

        # 데이터베이스에 데이터 저장
        df.to_sql("SalesData", con=engine, if_exists="replace", index=False, dtype=dtype_mapping)

        return {"message": "✅ CSV data uploaded successfully!"}

    except Exception as e:
        return {"error": str(e)}

# 데이터 조회 API
@app.get("/get-data/")
def get_data():
    try:
        # SQL Server 연결
        conn = pyodbc.connect(DB_CONNECTION_STRING)
        cursor = conn.cursor()

        # 데이터 조회
        cursor.execute("SELECT * FROM SalesData")
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        conn.close()

        return {"total_rows": len(data), "data": data}

    except Exception as e:
        return {"error": str(e)}

