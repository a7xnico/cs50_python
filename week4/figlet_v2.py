import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    set_font_based_on_input(figlet)
    message = input("Input: ")  # user message
    render_text(message, figlet)  # sends the message already rendered


def is_random_font():
    # without input it will be using a random font
    if len(sys.argv) == 1:
        return True
    # if the user adds 2 inputs and the first one is in the correct format
    elif len(sys.argv) == 3 and (sys.argv[1] in ("-f", "--font")):
        return False
    # extra inputs or wrong format
    else:
        handle_invalid_usage()


def handle_invalid_usage():  # handles all fail cases with a function
    print("Invalid Usage")
    sys.exit(1)


def random_conversion(figlet):  # randomizes within the availables fonts
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)  # sets the new font


def user_conversion(figlet):
    try:
        figlet.setFont(font=sys.argv[2])  # takes the font given by the user
    except ValueError: # not a valid font
        handle_invalid_usage()


def set_font_based_on_input(figlet):
    if is_random_font():  # checks if it's random or not
        random_conversion(figlet)  # converts the font randomly
    else:
        user_conversion(figlet)  # the user converts the font


def render_text(text, figlet):
    print("Output: ")
    print(figlet.renderText(text))  # the message from the user with the new font


main()
