import pandas as pd

udemy=pd.read_csv(r'C:\Users\Edgar\Documents\All Python\Python Data Analysis\Udemy Dataset\Udemy Courses.csv')

print(udemy.head())

#Q1 What are all differents subjets for with Udemy is offering courses

print('A1. List of subjets of Udemy courses')
#print(udemy.columns)
print([udemy['subject'].unique()])

#Q2 Which subject has the maximum number of courses

print('A2. Subject with the maximum number of courses')
print(udemy['subject'].value_counts())

#Q3 Show all the courses which are free of cost

print('A3. List of free courses')
print(udemy[udemy['is_paid']==False])

#Q4 Show all the courses which are paid

print('A4. List of paid courses')
print(udemy[udemy['is_paid']==True])

#Q5 Which are the top selling courses

print('A5. Top selling courses')
print(udemy.sort_values('num_subscribers', ascending=False))

#Q6 Which are the least selling courses
print('A6. Least selling courses')
print(udemy.sort_values('num_subscribers'))

#Q7 Show all courses of Graphic design where the price is below 100

print('A7. Courses of Graphic design with price below 100')
print(udemy[(udemy.subject == 'Graphic Design') & (udemy.price < '100')])
print(udemy[(udemy.subject == 'Graphic Design') & (udemy.price == '100')])

#Q8 List of the courses that are related with python

print('A8. Courses related to python')
print(udemy[udemy['course_title'].str.contains('Python')])

#Q9 What are courses that published in year 2015

print('A9. Courses published in 2015') 

print(udemy.dtypes)
print(udemy.published_timestamp)  
udemy.published_timestamp=pd.to_datetime(udemy.published_timestamp)  #convierte el tipo de dato de la columna Date a formato date-time
print(udemy.published_timestamp)
print(udemy.dtypes)
udemy['year']=udemy['published_timestamp'].dt.year
print(udemy[udemy['year']== 2015])

#Q10 What are the max number of subs for each level of course

print('A10. Max number of subs for each level of course')
print(udemy.groupby('level')['num_subscribers'].max())
print(udemy.groupby('level').max())