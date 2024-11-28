def main():
    greetings = input("Greeting: ").lower().strip()
    if starts_with(greetings):
        print("$0")
    elif first_letter(greetings):
        print("$20")
    else:
        print("$100")


def starts_with(answer):
    return answer.startswith("hello")  # Looks for hello in its entirety


def first_letter(answer):
    return answer.startswith("h")  # Looks for the letter H in the start of the input


main()
