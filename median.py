"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()

if(len(numbers) % 2 == 1):
    index = (len(numbers) + 1) / 2
    result = numbers[int(index-1)]

else:
    index = len(numbers) / 2
    result = (numbers[int(index)] + numbers[int(index) - 1]) / 2

print(result)
print(numbers)
