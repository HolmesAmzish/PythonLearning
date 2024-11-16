"""
program: fibonacci_generator.py
date: 2024-11-14
"""


def fibonacci_generator(start, end):
    a, b = 0, 1
    count = 0
    while count < end:
        if count >= start:
            yield b
        a, b = b, a + b
        count += 1


for fib_num in fibonacci_generator(10, 20):
    print(fib_num)