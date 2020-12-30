"""
To read the lines from a text file we use "open"
"""

with open('agenda.txt') as myfile:
    for line in myfile:
        print(line, end="")


with open('agenda.txt') as myfile:
    line_count = 0
    for line in myfile:
        line_count += 1

    print(line_count)

