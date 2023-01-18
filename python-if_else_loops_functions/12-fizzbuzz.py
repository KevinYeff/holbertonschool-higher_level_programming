#!/usr/bin/python3
def fizzbuzz():
    for nums in range(1, 101):
        if nums % 15 == 0:
            print("FizzBuzz", end=" ")
        elif nums % 3 == 0:
            print("Fizz", end=" ")
        elif nums % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(nums, end=" ")
