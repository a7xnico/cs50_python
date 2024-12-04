import sys
import random
from pyfiglet import Figlet

figlet = Figlet() # makes it easier to call in the program
if len(sys.argv) == 1: # if only run the program
    is_random_font = True # the font will be random
elif len(sys.argv) == 3 and (sys.argv[1] in ("-f", "--font")): # if used with these parameters
    is_random_font = False # the user will choose the font
else: # any other inputs
    print("Invalid usage")
    sys.exit(1)
if is_random_font == False:
    try:
        figlet.setFont(font=sys.argv[2]) # sets the font with the user input
    except:
        print("Invalid usage") # if not a valid font
        sys.exit(1)
else:
    random_font = random.choice(figlet.getFonts()) # gets a random font from the getFonts function
    figlet.setFont(font=random_font) # sets the font into the random font
message = input("Input: ") # the user input
print("Output: ")
print(figlet.renderText(message)) # the same input but with the added font

