from datetime import date

# Input date of birth
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# Today's date
today = date.today()

# Calculate age
age = today.year - birth_year

# Check if birthday has occurred this year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

# Output result
print("Your age is:", age)
