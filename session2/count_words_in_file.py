seen_words = {}

with open('mycoolfile.txt') as myfile:
    for line in myfile:
        # get all words from this line
        words = line.split()

        for word in words:
            print(f"Adding {word} to {seen_words}")
            seen_words.setdefault(word, 0)
            seen_words[word] += 1

            # try:
            #     seen_words[word] += 1
            # except KeyError:
            #     seen_words[word] = 1

print(seen_words)