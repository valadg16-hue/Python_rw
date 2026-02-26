print("Welcom to Interactive Personal Data Collector!")
name = input("Please enter your name:")
age = int(input("Please enter your age:"))
hight = float(input("Please enter your hight in meters:"))
number = int(input("Please enter your favorite number:")) 

print("Thank you! Here is the information we collected:")

print("Name:",name)
print("Memory Address :",id(name))
print("Age:",age)
print("Memory Address :",id(age))
print("Hight:",hight)
print("Memory Address :",id(hight))
print("Number:",number)
print("Memory Address :",id(number))

brithday_year = 2026 - age 
print("Your birth year is aprroximately:")
print(brithday_year,"(based on your age of)",age)

print("Thank you for using the Personal Data Colloector . Goodbye!")