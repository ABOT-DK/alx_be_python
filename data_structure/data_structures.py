numbers = [1,2,3, 4,7,9]

first, second, third, *remaining, last = numbers
print(remaining)
print(last)

for number in enumerate(numbers):
    print(number)