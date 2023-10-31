import random

min_val = int(input("Enter min number: "))
max_val = int(input("Enter max number: "))

while True:
    guess = num = random.randint(min_val, max_val)
    print(guess)
    hint = input("(l)Low, (h)High, (c)Correct, (q)QUIT")
    if hint.lower() == "l":
        max_val = guess
        continue
    elif hint.lower() == "h":
        min_val == guess
        continue
    elif hint.lower() == "c":
        break
    elif hint.lower() == "q":
        break