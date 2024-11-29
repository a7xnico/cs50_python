answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip() # error handling with .lower and .strip
match answer:
    case "42" | "forty-two" | "forty two": # Checks for all possible ways to say 42
        print("Yes")
    case _:
        print("No")
