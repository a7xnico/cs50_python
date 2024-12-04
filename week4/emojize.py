import emoji

text = input("Input: ") # gets the text from the user
output = emoji.emojize(text, language='alias') # alias for both _ and normal emoji names
print(f"Output: {output}") # gives the answer to the user
