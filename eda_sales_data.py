import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 정확한 파일 경로
file_path = r'C:\python\PythonProjects\RandyProject\data\sample-sales-data.csv'

# 데이터 불러오기
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# 기초 통계량 확인
print(df.describe())

# 결측값 확인
print(df.isnull().sum())

# 판매 데이터의 분포 확인
sns.histplot(df['SALES'], kde=True)  # 'Sales' 열을 확인하여 정확한 열 이름 사용
plt.title('Sales Distribution')
plt.show()

# 상관 관계 시각화
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 시간에 따른 판매 추세 시각화
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])  # 'ORDERDATE' 열 이름에 맞게 수정
df.set_index('ORDERDATE', inplace=True)
df['SALES'].resample('M').sum().plot()  # 'SALES' 열 이름에 맞게 수정
plt.title('Monthly Sales Trend')
plt.show()

# 제품별 판매 합계
sales_by_product = df.groupby('PRODUCT')['SALES'].sum().sort_values(ascending=False)  # 'PRODUCT'와 'SALES'로 수정
print(sales_by_product)