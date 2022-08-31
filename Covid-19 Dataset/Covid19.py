import pandas as pd
import seaborn as sns  #Libreria que funciona sobre matplot, agrega mas opciones para  visualizar datos
import matplotlib.pyplot as plt   #libreria para visualizr datos

covid=pd.read_csv(r"C:\Users\Edgar\Documents\Python Data Analysis\Covid-19 Dataset\Covid_19_data.csv")

print(covid.head())
print(covid.count())
print(covid.isnull().sum())

#sns.heatmap(covid.isnull())  Muestra un grafico de calor
#plt.show()                   funcion para graficar la linea de comando anterior

#Q1 Sshow the number of confirmed death an recovered in each region

print('A1.Number of confirmed death and recovered in each region')
print(covid.groupby('Region').sum().head(20))
print(covid.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(20))  #muestra las cosas confirmado de mayor a menor
print(covid.groupby('Region')['Confirmed','Deaths'].sum()) # muestra los casos de confirmados y Muertes

#Q2 Remove all the records where confirmed is less then 10

print('A2. Records where confirmed is above then 10')
print(covid[covid.Confirmed < 10])
print(covid[~(covid.Confirmed < 10)].head(50))
# covid=covid[~(covid.Confirmed < 10)].head(50) de esta forma se remueve valores de forma permanente

#Q3 In which region, maximun number of Confirmed is recorded

print('A3. Region with maximun number of confirmed recorded')
print(covid.groupby('Region').Confirmed.sum().sort_values(ascending=False).head(20))

#Q4 In which region, mminimun number of Deaths is recorded

print('A4. Region with maximun number of Deaths recorded')
print(covid.groupby('Region').Deaths.sum().sort_values(ascending=True).head(50))

#Q5 How many confirmed, deaths and recovered cases were recorded in india

print('A5. Number of confirmed, deaths and recovered cases recorded in india')
print(covid[covid.Region=='India'])

#Q6-a Sort the entire data by confirmed cases in ascending order

print('A6-a. Confirmed cases in ascending order')
print(covid.sort_values(by=['Confirmed'], ascending=True))

#Q6-b Sort the entire data by Deaths cases in descending order

print('A6-b. Deaths cases in descending order')
print(covid.sort_values(by=['Deaths'], ascending=False))