



# Coffee break until 13:10

class Accumulator:
    def __init__(self):
        self.total = 0

    def add(self, number):
        self.total += number

s1 = Accumulator()
s2 = Accumulator()

s1.add(10)
s2.add(50)
s1.add(20)
s2.add(70)
s1.add(30)


# Prints: 60
print(s1.total)

# Prints: 120
print(s2.total)
