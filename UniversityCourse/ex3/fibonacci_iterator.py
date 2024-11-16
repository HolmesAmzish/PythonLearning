"""
program: get list of specialized fibonacci numbers list
date: 2024-11-14
"""


class FibonacciIterator:
    def __init__(self, start, end):
        self.a, self.b = 0, 1
        self.start = start
        self.end = end
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.end:
            raise StopIteration
        while self.count < self.start:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return self.a


fibonacci_iterator = FibonacciIterator(10, 20)
for num in fibonacci_iterator:
    print(num)
