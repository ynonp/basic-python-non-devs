import re

pattern = r'(one|two|three|four|five|six|seven) ([a-z]+) went to (hunt|play|sleep)'
text = 'five elephants went to hunt'

match = re.search(pattern, text)
print(match.groups())
#match.group(1)

resolution = '1024x768'
width, height = re.search(r'([0-9]+)x([0-9]+)', resolution).groups()
print(f"Your screen is {width} pixels wide and {height} pixels high")
