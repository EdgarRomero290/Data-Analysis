import pandas as pd

car=pd.read_csv(r"C:\Users\Edgar\Documents\All Python\Python Data Analysis\Cars\Cars Data.csv")
print(car.info)

# Q1 Find the null values in the dataset and if there is one filled with the mean of the column

print('A1. Amount of NULL  values')
print(car.isnull().sum())

#car['Cylinders'].fillna(car['Cylinders'].mean()) solo aplica columnas con valores int o float, 
car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True) #hace el cambio permanete

#Q2 Find the amount of ocurrence and types of "Make"
print('A2. Amount of ocurrence and type of Make')
print(car['Make'].value_counts())

#Q3 Find the amount of origin from "Asia" or "Europe"

print('A3. Amount of origin from Asia or Europa')
#print(car[(car['Origin']=='Asia') | (car['Origin']=='Europe')])
#Otra forma
print(car[car['Origin'].isin(['Asia','Europe'])]) 

#Q4 Remove all values if Weight is above 4000

print('A4. Values of Weight below 4000')
#print(car[car['Weight']>4000]) #muestra valores sobre 4000
print(car[~car['Weight']>4000]) #muestra valores por debajo de 4000

#Q5 increase the values of MPG_city by 3

print('A5. Values of MPG_city increased by 3')
car['MPG_City'] = car['MPG_City'].apply(lambda x: x+3)
print(car)



