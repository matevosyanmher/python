class CountFromBy:
    def __init__(self, low, high, step=1):
        self.val = low
        self.high = high
        self.step = step

    def increase(self) -> None:
        self.val += self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.val > self.high:
            raise StopIteration
        else:
            current = self.val
            self.increase()
            return current


if __name__ == '__main__':
    counter = CountFromBy(0, 10)
    print(list(counter))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

