fruits = ['apple', 'banana', 'orange']

print(fruits)
print(len(fruits))

fruits.append("watermelon")
fruits += ['avocado', 'plum']

print(fruits)

if 'avocado' in fruits:
    print("Yay it's winter")


for fruit in fruits:
    print(f"I like to eat {fruit}")


for index, fruit in enumerate(fruits):
    print(f"{index} likes to eat {fruit}")


print(fruits[0])

