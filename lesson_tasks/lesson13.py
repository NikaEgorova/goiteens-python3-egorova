class Alphabet:
    def __init__(self):
        self.list = list

    def print_letters(self):
        print(self.list)

    def count_letters(self):
        print(len(self.list))

    def last(self):
        print(self.list[-1])


list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
myAlphabet = Alphabet()
myAlphabet.print_letters()
myAlphabet.count_letters()
myAlphabet.last()
