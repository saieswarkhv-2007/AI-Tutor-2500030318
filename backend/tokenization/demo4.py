word = input("Enter a word:") or "Python"

print("word:",word)
print("Length of the word:",len(word))

characters = list(word)
print("Character in the given word:",characters)

pairs = list(zip(characters,characters[1:]))

print("Adjacent pairs:",pairs)