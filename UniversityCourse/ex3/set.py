"""
program:
date: 2024-11-14
"""

import random

A = {random.randint(0, 10) for _ in range(10)}
B = {random.randint(0, 10) for _ in range(10)}

print(f'''
        A: {A}
        B: {B}
        Length of A: {len(A)}
        Length of B: {len(B)}
        Max of A: {max(A)}
        Min of A: {min(A)}
        Max of B: {max(B)}
        Min of B: {min(B)}
        Union of A and B: {A | B}
        Intersection of A and B: {A & B}
        Difference of A and B: {A - B}
''')
