class Accumulator:
    def __init__(self):
        pass

    def add(self, number):
        pass

s1 = Accumulator()
s2 = Accumulator()

s1.add(10)
s1.add(20)
s1.add(30)

s2.add(50)
s2.add(70)

# Prints: 60
print(s1.total)

# Prints: 120
print(s2.total)
