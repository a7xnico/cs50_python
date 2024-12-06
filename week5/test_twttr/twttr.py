def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    output = ""
    for c in word:
        if c.lower() not in vowels:
            output += c
    return output


if __name__ == "__main__":
    main()
