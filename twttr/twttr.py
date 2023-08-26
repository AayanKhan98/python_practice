tweet = str(input("Input: "))
vowel = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
for c in tweet:
    if (c in vowel):
        print(end="")
    else:
        print(c, end="")
print("")