class Test:
    def __init__(self):
        self.deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < len(self.deck):
            x = self.deck[self.a]
            self.a += 1
            return x
        else:
            raise StopIteration


testObject = Test()
for item in testObject:
    print(item)
