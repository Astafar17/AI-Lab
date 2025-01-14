
def determine_division(percentage):
    if percentage >= 80:
        return "Distinction"
    elif percentage >= 65:
        return "First Division"
    elif percentage >= 55:
        return "Second Division"
    elif percentage >= 40:
        return "Third Division"
    else:
        return "Fail"


percentage = float(input("Enter your percentage: "))


if 0 <= percentage <= 100:
    division = determine_division(percentage)
    print(f"Your division is: {division}")
else:
    print("Invalid percentage! Please enter a value between 0 and 100.")
