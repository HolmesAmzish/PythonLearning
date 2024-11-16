"""
date: 2024-11-14
"""


def sum_repeat(a, n):
    result, term = 0, 0
    for i in range(n+1):
        term += term * 10 + a
        result += term

    return result


a = int(input("Enter a number: "))
n = int(input("Enter time: "))
print("Result: ", sum_repeat(a, n))