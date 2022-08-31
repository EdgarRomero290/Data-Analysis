import pandas as pd
import seaborn as sns  #Libreria que funciona sobre matplot, agrega mas opciones para  visualizar datos
import matplotlib.pyplot as plt   #libreria para visualizr datos

london=pd.read_csv(r"C:\Users\Edgar\Documents\All Python\Python Data Analysis\London Housing Dataset\London Housing data.csv")

print(london.isnull().sum())
print(london.count())


#Q1 Convert the datatype of column Date to Date-time format

print('A1. Datatype of column Date to Date-time format')
print(london.dtypes)                        #Muestra el tipo de dato que contiene las columnas
london.date=pd.to_datetime(london.date)     #Convierte el tipo de dato de la columna Date a formato date-time
print(london.date)

#Q2 Add a new column Year in the dataframe, which contains only year

print('A2. New column Year in the dataframe, which contains only year')
london['year']= london.date.dt.year         #Crea una nueva columna con el nombre de Year
#print(london.head(3))

#Q3 Add a new column Month as 2nd column in the dataframe, which contains only month

print('A3. New column Month as 2nd column in the dataframe, which contains only month')
london.insert(1, 'month', london.date.dt.month)         #Crea una colunma months en el indice 2 del dataframe
print(london.head(3))

#Q4 Remove the columns Year and Months from the dataframe

print('A4. Remove the columns Year and Months from the dataframe')
#london.drop(['year', 'month'], axis=1, inplace=True)   #Elimina las columnas year y month
print(london.head(3))

#Q5 Show the record where the Number of Crimes are 0 and how many of this records are there

print('A5. Record where the No of Crimes are 0 and how many of this records are there')
print(london[london['no_of_crimes']==0])        #Muestra el numero de casos donde el numero de d crimenes es 0
print(london['no_of_crimes'].isnull().sum())    #Muestra la cantidad de valores null en la columna
print(len(london[london['no_of_crimes']==0]))   #Muestra la cantidad de casos donde numero de crimenes es 0

#Q6 What is the maximum and minimum average price per year in England

print('A6. Maximum and minimum average price per year in England ')

data=london[london['area'] =='england']
print(data.head())
print(data.groupby('year').average_price.max())
print(data.groupby('year').average_price.min())
print(data.groupby('year').average_price.mean())

#Q7 What the maximum and minimum number of crimes recorded per area

print('A7. Maximum and minimum no of crimes recorded per area')
print(london.groupby('area').no_of_crimes.max())
print(london.groupby('area').no_of_crimes.max().sort_values(ascending=True))
print(london.groupby('area').no_of_crimes.min().sort_values(ascending=True))

#Q8 Show the total count of records of each area where the average price is less than 100000

print('A8. Total count of records of each area where the average price is less than 100000')
print(london[london.average_price<100000].area.value_counts()) 
#Muestra el numeco de casos donde el precio promedio es menor a 100000, de acuerda al area



