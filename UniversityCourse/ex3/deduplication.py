"""
program: deduplication.py
date: 2024-11-16
"""


def unique_sorted(sentence):
    words = sentence.split()
    unique_words = sorted(set(words))
    # print(" ".join(unique_words))
    return unique_words


sentence = "hello world and practice makes perfect and hello world again"
print(unique_sorted(sentence))
