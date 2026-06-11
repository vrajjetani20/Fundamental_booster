
print("Welcome to personal data collector:")

print("\n")


Name = str(input("Enter your name:"))
Age = int(input("Enter your age:"))
Hight = float(input("Enter your hight:"))
Favourit_number = int(input("Enter your fav num:"))

print("\n")

print("Thank you , give your personal information")

print("\n")

print("Name:",Name ,"type:",type(Name),"id:(Adress)",id(Name))
print("Age:",Age,"type:",type(Age),"id:(Adress)",id(Age))
print("Hight:",Hight ,"type:",type(Hight),"id:(Adress)",id(Hight))
print("Favourit_number:",Favourit_number,"type:",type(Favourit_number),"id:(Adress)",id(Favourit_number))

print("\n")

year = 2026
final_year = year - Age 
print("Your birth year is  approx:",final_year,"Based on your age of",Age)
print("\n")

print("Thank you! for Give The Time Data Collector.Goodbye" )
