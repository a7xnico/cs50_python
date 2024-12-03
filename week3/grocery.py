grocery_list = {} # creates the grocery list

def main():
    while True: # loops through the list
        try:
            grocery = input("")
            if grocery in grocery_list:
                grocery_list[grocery] += 1 # gives the value to the key when it's repeated
            else:
                grocery_list[grocery] = 1 # sets the value to 1
        except EOFError:
            count = 0 # to search the highest value for that key
            item = "" # gets the key name
            for grocery in grocery_list: # searches through every one
                if grocery_list[grocery] > count: # if higher than the count variable
                    count = grocery_list[grocery] # new value
                    item = grocery
            for item in sorted(grocery_list): # sorts alphabetically
                print(f"{grocery_list[item]} {item.upper()}") # gets the value and the name in uppercase
            break


main()
