import pandas as pd

# 파일 경로
file_path = r'C:\python\PythonProjects\RandyProject\data\sample-sales-data.csv'

# 데이터 불러오기
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# 1. 중복된 행 제거 (기본적으로 모든 열을 기준으로 중복 검사)
df_deduplicated = df.drop_duplicates()

# 2. 특정 열을 기준으로 중복 제거 (예: ORDERNUMBER)
df_unique = df_deduplicated.drop_duplicates(subset=['ORDERNUMBER'])

# 3. 데이터 무결성 검증: ORDERNUMBER가 유일해야 한다는 가정 하에 검증
if df_unique['ORDERNUMBER'].is_unique:
    print("ORDERNUMBER is unique across the dataset!")
else:
    print("There are duplicate ORDERNUMBER values!")

# 4. 결측값 확인 및 처리
# ORDERNUMBER와 SALES 열에 결측값이 있을 경우 해당 행을 삭제
df_cleaned = df_unique.dropna(subset=['ORDERNUMBER', 'SALES'])

# 5. 결과를 CSV로 저장
df_cleaned.to_csv(r'C:\python\PythonProjects\RandyProject\data\sample-sales-data_cleaned.csv', index=False)

print(f"Before deduplication: {df.shape}")
print(f"After deduplication and cleaning: {df_cleaned.shape}")