#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

# Calling the happy_new_year function
happy_new_year()


 

def square_integers(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num ** 2)
    return squared_list

# Calling the square_integers function
result = square_integers([1, 2, 3, 4, 5])
print(result)

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")   
        else:
            print(num)

fizzbuzz()