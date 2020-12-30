def my_max1(x, y, z):
    return max(x, y, z)


def my_max2(x, y, z):
    result = x
    for i in [y, z]:
        if i > result:
            result = i
    return result


def first_letters(w1, w2, w3):
    return w1[0] + w2[0] + w3[0]


print(my_max2(10, 20, 5))
print(first_letters("one", "two", "three"))