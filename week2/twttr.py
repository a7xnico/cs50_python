text = input("Input : ")  # asks for the initial input
vowels = ["a", "e", "i", "o", "u"]  # makes a list of vowels to look later in the loop
print("output: ", end="")
for c in text:
    if c.lower() not in vowels:  # only prints when the character isn't a vowel
        print(c, end="")
print()  # prints a final line
