# File Handle
with open('demo.txt', encoding='utf8') as file:
    max_line_length = 0

    for line in file:
        if len(line) > max_line_length:
            max_line_length = len(line)

    print(max_line_length)


