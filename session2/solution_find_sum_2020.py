values = []
with open('input.txt') as file:
    for line in file:
        values.append(int(line))


def part1():
    for i in values:
        for j in values:
            if i != j and i + j == 2020:
                print(f"Found! {i}, {j}")
                return


def part2():
    for i in values:
        for j in values:
            for k in values:
                if i != j and j != k and i + j + k == 2020:
                    print(f"Found! {i}, {j}, {k}")
                    return

part1()
part2()

