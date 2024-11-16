"""
program: guess.py
date: 2024-11-14
"""
import random

# Generate a random even number
target = random.choice(range(0, 101, 2))
while True:
    guess = int(input("Guess a number: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    if guess == target:
        print("You got it!")
        break