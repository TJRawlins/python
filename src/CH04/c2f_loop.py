while True:
    c = input("Enter a celcius or q to quit: ")
    if c == "q" or c == "Q":
        break
    elif c == "":
        print("Must enter something")
        continue
    else:
        f = ((9 * float(c)) / 5) + 32
        print(f)