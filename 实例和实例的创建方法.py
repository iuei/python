class Basic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b


i = Basic(1, 2)
print(i.a, i.b, i.sum())
