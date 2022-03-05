#it will take age as input from user
age = input("What is your current age?")

#this tell us how many days, weeks, and months are left 
years = 90 - int(age)
days = round(years * 365)
week = round(years * 52)
month = round(years * 12)

#prints the final output
print(f"You have {days} days, {week} weeks, and {month} months left.")
