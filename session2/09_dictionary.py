"""
A Dictionary is like a "set" but each item also has a "value"

It's great for storing data on an attached value for known keys
(for example for counting, or managing related data)
"""

# Define a dictionary with {}
d = { 'apple': 'red', 'lettuce': 'green', 'lemon': 'yellow', 'cucumber': 'green' }

# Access a specific item by key using square brackets:
print(d['apple'])

# Modify an item by key using square brackets:
d['lettuce'] = 'blue'

# Iterate and print all key/value pairs from the dictionary:
for key, value in d.items():
    print(f"{key} is {value}")

