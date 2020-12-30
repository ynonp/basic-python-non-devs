read_lines = []

with open('mycoolfile.txt') as myfile:
    for line in myfile:
        print(line, end="")
        if line in read_lines:
            break
        else:
            read_lines.append(line)

