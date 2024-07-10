characters = [character for character in input() if character != " "]
letters = {}
for character in characters:
    if character not in letters.keys(): #if character not in letters
        letters[character] = 0
    letters[character] += 1
for symbol, occurrences in letters.items():
    print(f"{symbol} -> {occurrences}")