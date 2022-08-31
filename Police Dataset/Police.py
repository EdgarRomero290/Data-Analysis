import pandas as pd

police=pd.read_csv(r"C:\Users\Edgar\Documents\All Python\Python Data Analysis\Police Dataset\Police Data.csv")

print(police.info())

#Q1 Remove the column that only contains missing values

print('A1. Remove the column that only contains missing values')
print(police.isnull().sum())
police.drop(columns='search_type', inplace= True) #forma de eliminar columnas
police.drop(columns='country_name', inplace= True)
print(police.head())

#Q2 For speeding, were women or men more offen stop

#Primero toma la columna violation y filtra el valor Speeding, luego a esta columna filtrada se compara en la columna driver_gender
#Aplicando un value_count, la cual muestra los unicos de la columna driver_gender y el numero de veces que se repite

print('A2. Amount of speeding stops between women or men')
print(police[police.violation=='Speeding'].driver_gender.value_counts()) 
#print(police[police.violation=='Speeding'].driver_gender.sum())

#Q3 Does gender affect who gets searched during stop

print('A3. Amount of searched during stops between women or men')
print(police.groupby('driver_gender').search_conducted.sum())
print(police.search_conducted.value_counts())

#Q4 Whats the mean of stop_duration

#La columna stop_duration tiene valores de tipo string, parca calcular el mean se deben cambiar los valores a tipo int
#para eso se utiliza al funcion .map({old:new})

print('A4. Mean of stop_duration')
police['stop_duration']=police['stop_duration'].map( { '0-15 Min': 7.5, '16-30 Min': 24, '30 + Min': 45 })
print(police.stop_duration.mean())

#Q5 Compare the age distribution each violation

print('A5. Age distribution of each violation')
print(police.groupby('violation').driver_age.describe())
#La funcion .describe() muestra el mean, la cuenta, Standart Deviation, max y min de cada valor unico de la columna violation


