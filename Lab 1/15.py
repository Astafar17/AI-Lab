#15) Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
'''
class person:
    Name='',
    country='',
    DOB='',
    todaysDate=2024
    age()
    {
        todaysDate-DOB
    }


person.DOB=(input("enter the date of birth  of a person"))
todaysDate=(input("enter todays date"))

age= age()

print(f"age is{age} ")

'''


from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # Date of birth in YYYY-MM-DD format

    def calculate_age(self):
        # Extract the current year
        current_year = datetime.now().year
        # Extract the birth year from dob
        birth_year = int(self.dob.split('-')[0])
        # Calculate the age
        return current_year - birth_year

# Example usage:
# Input details
name = input("Enter the person's name: ")
country = input("Enter the person's country: ")
dob = input("Enter the person's date of birth (YYYY-MM-DD): ")

# Create a Person object
person = Person(name, country, dob)

# Calculate and display the age
age = person.calculate_age()
print(f"{person.name} from {person.country} is {age} years old.")
