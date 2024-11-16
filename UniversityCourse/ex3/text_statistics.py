"""
program: text statistics
date: 2024-11-16
"""
import re


def text_statistics(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    paragraphs = text.split('\n\n')
    lines = text.splitlines()
    sentences = re.findall(r'[.!?]', text)
    words = re.findall(r'\w+', text)

    word_count = {word: words.count(word) for word in set (words)}

    print("Paragraph:", len(paragraphs))
    print("Lines:", len(lines))
    print("Sentences:", len(sentences))
    print("Words:", len(words))
    print("Word count:", len(word_count))


text_statistics("abstract.txt")

