from numpy import place
import pandas as pd
import seaborn as sns  #Libreria que funciona sobre matplot, agrega mas opciones para  visualizar datos
import matplotlib.pyplot as plt   #libreria para visualizr datos
\

netflix=pd.read_csv(r'C:\Users\Edgar\Documents\All Python\Python Data Analysis\Netflix Dataset\Netflix Dataset.csv')

#1
print(netflix.head())
#2
print(netflix.tail())
#3
print(netflix.shape)
#4
print(netflix.size)
#5
print(netflix.columns)
#6
print(netflix.dtypes)
#7
print(netflix.info())

#Task 1 Is there any Duplicate Records in this dataset? if yes, then remove the duplicate records

print('Task1. Remove the duplicate records')
netflix.drop_duplicates(inplace=True)
print(netflix[netflix.duplicated()])

#Task 2 is there any Null Value present in any column? Show with heat-map
#print(netflix.isnull().sum())
#sns.heatmap(netflix.isnull())  
#plt.show() 

#Q1 For 'House of Cards', what's the Shows ID and Who is the diredtor is this show?
print('A1. House of cards ID and Director')
print(netflix[netflix['Title'].isin(['House of Cards'])])           #1er metodo
print(netflix[netflix['Title'].str.contains('House of Cards')])     #2do metodo

#Q2 In which year the highest number of TV Shows and Movies were release?

print('A2. Year with the highest number of TV Shows and Movies released')
netflix['Release_Date']=pd.to_datetime(netflix['Release_Date'])
print(netflix['Release_Date'].dt.year.value_counts())
#netflix['Release_Date'].dt.year.value_counts().plot(kind='bar'))

#Q3 How may Movies ad TV series are in this dataset

print('A3. Amount of Movies ad TV series in the dataset ')
print(netflix.groupby('Category').Category.count())

#sns.countplot(netflix['Category'])  
#plt.show()

#Q4 Show all the movies that were release in year 2000

print("A4. Movies of the 2000's")
netflix['Year']=netflix['Release_Date'].dt.year
print(netflix[(netflix['Category']=='Movie') & (netflix['Year']==2000)])

#Q5 Show only the title of all TV shows that were released only in india 
print('A5. TV shows released only in india')
print(netflix[(netflix['Category']=='TV Show') & (netflix['Country']=='India')]['Title'])

#Q6 Show top 10 Directors, who have the hightest number of TV Shows and Movies on Netflix

print('A6. Top 10 Directors')
print(netflix['Director'].value_counts().head(10))

#Q7 Show all the records, where Category is Movie and type is Comedies or country is UK

print('A7. Records of Comedy Movie or country is UK')
print(netflix[((netflix['Category']=='Movie') & (netflix['Type']=='Comedies')) | (netflix['Country']=='United Kingdom')])

#Q8 In how many TV Shows/Movies, Tom Cruise was cast

print('A8. Tom Cruise filmography')
print(netflix[netflix['Cast']=='Tom Cruise'])

netflixData =netflix.dropna()

print(netflixData[netflixData['Cast'].str.contains('Tom Cruise')])

#Q9 What are the different ratings defined by netflix

print('A9. Ratings defined by netflix')
print(netflix['Rating'].nunique())
print(netflix['Rating'].unique())

#Q9-1 How many movies got the TV-14 rating, in Canada

print('A9-1. Amount of TV-14 Movies in Canada')

print(netflix[(netflix['Country']=='Canada') & (netflix['Rating']=='TV-14') & (netflix['Category']=='Movie')].shape )

#Q9-2 How many TV Shows got the R rating, after year 2018

print('A9-2. Amount of R rating TV shows, after year 2018')
print(netflix[(netflix['Year']>2018) & (netflix['Rating']=='R') & (netflix['Category']=='TV Show')])

#Q10 Whats the maximum duration of a Movie/TV Show on Netflix

print('A10. Maximum duration of a Movie/TV Show on Netflix')
print(netflix['Duration'].unique())
print(netflix['Duration'].dtype)
netflix[['Minutes', 'Unit']]= netflix['Duration'].str.split(' ',expand=True)
print(netflix.head(2))
print(netflix.Minutes.max())

#Q11 Which individual country has the highest Number of TV Shows

print('A11. Country with the highest Number of TV Shows ')
netflixTV= netflix[netflix['Category']=='TV Show']
print(netflixTV.Country.value_counts())

#Q12 How can we sort de dataset by year

print('A12. Dataset sorted by year')
print(netflix.sort_values(by='Year').head())
print(netflix.sort_values(by='Year', ascending=False).head())

#Q13 Fins all instances where Category is Movies and type drama or category is Tv Shows and type is Kids TV

print("A13-a. List of Drama TV Shows")
print(netflix[(netflix['Category']=='TV Show') & (netflix['Type']=="Kids' TV")])

print("A13-b. List of Drama Movies")
print(netflix[(netflix['Category']=='Movie') & (netflix['Type']=='Dramas')])

print('A13-c. List of Drama Movies and TV Shows')
print(netflix[((netflix['Category']=='Movie') & (netflix['Type']=='Dramas')) | ((netflix['Category']=='TV Show') & (netflix['Type']=="Kids' TV"))])