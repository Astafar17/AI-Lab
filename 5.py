# Function to input and display marks of 10 students
def enter_and_display_marks():
    marks = []  # List to store marks
    for i in range(1, 11):
        mark = float(input(f"Enter marks for student {i}: "))
        marks.append(mark)
    
    # Display the marks
    print("\nMarks of 10 students:")
    for i, mark in enumerate(marks, start=1):
        print(f"Student {i}: {mark}")

# Call the function
enter_and_display_marks()
