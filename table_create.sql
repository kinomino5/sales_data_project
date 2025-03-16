USE MyDatabase;

CREATE TABLE TitanicData (
PassengerId INT PRIMARY KEY,
Survived INT,
Pclass INT,
Name NVARCHAR(255),
Sex NVARCHAR(50),
Age FLOAT,
SibSp INT,
Parch INT,
Ticket NVARCHAR(50),
Fare FLOAT,
Cabin NVARCHAR(50),
Embarked NVARCHAR(50)
);