read_lines = []

with open('mycoolfile.txt') as my_file:
    for line in my_file:
        if line not in read_lines:
            read_lines.append(line)
        else:
            break

        print(line, end="")


