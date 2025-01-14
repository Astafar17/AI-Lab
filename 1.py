
def odd_even(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

num = int(input("Enter a number: "))

result = odd_even(num)
print(result)
