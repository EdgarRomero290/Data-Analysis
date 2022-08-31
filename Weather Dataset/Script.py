import pandas as pd

data=pd.read_csv(r"C:\Users\Edgar\Documents\Python Data Analysis\Weather Dataset\Weather Data.csv") # Asigna un dataset a una variable


data.head(3)                #.head() muestra filas, por default es 5

data.shape                  #.shape muestra en numero total de filas y columnas

data.index                  #.index muestra el indice del dataframe

data.columns                #.columns muestra la cantidad de columnas en forma de lista

data.dtypes                 #.dtypes muestra el tipo de dato de cada columna

data['Weather'].unique()    #.unique() muetra los valores UNICOS, se aplica en una sola columna

data.nunique()              #.nunique() muetra el numero de valores UNICOS en cada columna

data.count()                #.count() muestra el numero total de no-null valores en cada columna. Se puede aplicar a una columna o a todo el dataframe

data['Weather'].value_counts()      #.value_count() muestra los valores unicos en una sola columna y el numero que debes que se repite
data.Weather.value_counts()


print(data.info())          #.info() muestra informacion basica del dataframe

#Q1. Find all the wind speed unique values en the data

print('A1. Unique values of wind speed ')
print(data['Wind Speed_km/h'].unique())

#Q2. Find the numbers of times weather is exactly clear

#Aqui aplicamos FILTERING Y GROUPBY
print(' A2. Nnumbers of times  weather is exactly clear')
print(data[data.Weather == 'Clear'])  #FILTERING
#print(data.groupby('Weather').get_group('Clear'))  GROUPBY

#Q3. Find the number of times the wind speed was 4km/h

print(' A3. Number of times the wind speed was 4km/h')
print(data[data['Wind Speed_km/h'] == 4])

#Q4 Find the number of NULL values en data

print(' A4. Number of NULL values en dataa')

print(data.isnull())            #Muestra los valores NULL en forma de bool
print(data.isnull().sum())      #Muestra los valores NULL en formade int
print(data.notnull().sum())     #Muestra los valores NoNull en data, en forma de int

#Q5 Rename the Weather Column 

print('Q5. Rename the weather column')
print(data.rename(columns={'Weather':'Weather Condition'}))     #Solo se renombra para la ejecucion, la data original no cambia
##print(data.rename(columns={'Weather':'Weather Condition'}, inplace=True)) para hacer el cambio permanente se agrega el inplace=True

#Q6 What is mean Visibility

print('A6. Mean Visibility')
print(data.Visibility_km.mean())    #.mean()

#Q7 Whats the Standart Deviation of Pressure

print('A7. Standart Deviation of Pressure')
print(data.Press_kPa.std())         #.std()

#Q8 Whats the Variance of Relative Humidity

print('A8. Variance of relative humidity')
print(data['Rel Hum_%'].var())      #.var()

#Q9 Find number of times Snow is recorded

print('A9. Number of times Snow is recorded')
print(data[data['Weather'] == 'Snow'])              #primera forma

print(data[data['Weather'].str.contains('Snow')])   #segunda forma usando str.contain

#Q10 Find all instances when wind speed is above 24 anf visibility is 25'

print('A10. Wind speed is above 24 anf visibility is 25')
print(data[(data['Wind Speed_km/h'] >24) & (data['Visibility_km'] == 25)])

#Q11 Whats the mean of each columns against each Wheather

print('A11. Mean of each columns against each Wheather')
print(data.groupby('Weather').mean())

#Q12 Minimun and max value of each column on each weather

print('A12-a. Minimun value of each column on each weather')
print(data.groupby('Weather').min())

print('A12-b. Max value of each column on each weather')
print(data.groupby('Weather').max())

#Q13 Find number of times Fog is recorded

print('A13. Number of times Fog is recorded')
print(data[data['Weather'].str.contains('Fog')])

#Q14 Find all instances when weather is clear and visibility is above 40'

print('Q14. Instances when weather is clear and visibility isa above 40')
print(data[(data['Weather'] =='Clear') | (data['Visibility_km'] > 40)])

#Q15 Find all instances when weather is clear and relative humidity  is above 50 or visibility is above 40

print('Q15. Instances when weather is clear and relative humidity is above 50 or visibility isa above 40')
print(data[((data['Weather']=='Clear') & (data['Rel Hum_%']>50)) | (data['Visibility_km'] > 40)])

