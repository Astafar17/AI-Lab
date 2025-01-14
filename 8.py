#8)WAP to sort the list {51,4,11,13,5}
"""
list=[51,4,11,13,5]
list.sort()
print(list)
list.sort(reverse=True)
print(list)


"""



numbers = [51, 4, 11, 13, 5]
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        # Swap if the element found is greater than the next element
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


print("Sorted list:", numbers)

