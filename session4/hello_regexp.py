import re

## Coffee break until 11:00

## Then:
## Modify this program to print ONLY the lines which end with :
## i.e. print only these lines:
##
## Link To Slides:
## Daily Agenda:


# Search for a "full match" - all text must match the regexp
#re.match()

# Search the pattern in the text (like we saw in the demos)
#re.search()

with open('agenda.txt') as file:
    for line in file:
        if re.search(r'[0-9]\.', line):
            print(line, end="")
