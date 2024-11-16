"""
program: dict.py
date: 2024-11-14
"""


def create_dict(list1, list2):
    length = min(len(list1), len(list2))
    result = dict(zip(list1[:length], list2[:length]))
    return result


l1 = input("Enter first list: ").split()
l2 = input("Enter second list: ").split()
dictionary = create_dict(l1, l2)
print(dictionary)
