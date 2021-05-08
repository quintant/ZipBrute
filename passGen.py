import string
from random import shuffle

class PassGen:
    def __init__(self, size: int=1000, _shuffle:bool=True):
        self.bank = list()
        self.size = size
        print('Loading passwords')
        with open('rockyou.txt', encoding="ansi") as f:
            for word in f.readlines():
                word = word.strip()
                word = word.strip(string.whitespace + "\n\r")
                self.bank.append(word)
        if _shuffle:
            print('Shuffling passwords')
            shuffle(self.bank)
        self.pos = 0

    def get(self):
        tmp = self.bank[self.pos: self.pos + self.size]
        self.pos += self.size
        return tmp

    def split(self, n:int=6):
        length = len(self.bank)
        splitSize = length // n
        items = []
        for i in range(0, n-1):
            items.append(self.bank[i*splitSize: (i+1) * splitSize])
        items.append(self.bank[(n-1)*splitSize:])
        return items


