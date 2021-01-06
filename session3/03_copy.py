# Write a program that creates a new copy of a file:
#
# Copy all the lines from file A -> file B
import os
with open('agenda.txt', encoding='utf8') as fin, \
    open('copy.txt', 'w', encoding='utf8') as fout:
        for line in fin:
            outline = line.replace("-", "*")
            fout.write(outline)

os.replace("copy.txt", "agenda.txt")

