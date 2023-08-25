import datetime
#Birth year calculator

#output ask for name
print('What is your name?')
#accept input and store in string var
name = input()
#output ask for age
print('What is your age?')
#accept input and store in int var
age = int(input())
#calc today's year
today = datetime.date.today()
year = today.year
#convert year to int

#subtract today's year by age
born = year - age
born_year = str(born)
#print name and age
print('Hello '+ name +'! You were born in '+ born_year+'.')