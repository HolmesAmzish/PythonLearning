"""
date: 2024-11-14
"""

import random

ls = [random.randint(10, 99) for _ in range(10)]
sorted_ls = sorted(ls, reverse=True)
print(sorted_ls)

average = sum(ls) / len(ls)
print('The average:', average)

for i in ls:
    if i >= average:
        print(i, end=' ')