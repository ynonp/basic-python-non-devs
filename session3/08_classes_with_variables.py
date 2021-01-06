class Kitten:
    def __init__(self, name):
        # self.name = f"[Kitten] {name}"
        self.name = name
        self.age = 0

    def come_here(self):
        print(f"Come here kitten ... {self.name}")
        self.xxx = 10


k1 = Kitten("kitty")
k1.come_here()

k1.yyy = 20

print(k1.name)



