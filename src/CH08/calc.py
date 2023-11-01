def add(exp):
    print(int(exp[0]) + int(exp[2]))

def subtract(exp):
    print(int(exp[0]) - int(exp[2]))

def divide(exp):
    print(int(exp[0]) / int(exp[2]))

def multiply(exp):
    print(int(exp[0]) * int(exp[2]))

while True:
    exp = input("Please enter math expression or (q)QUIT: ")
    if exp == "":
        continue
    elif exp.lower() == "q":
        break
    else:
        exp_arr = exp.split(" ")
        if exp_arr[1] in "+":
            add(exp_arr)
            continue
        elif exp_arr[1] in "-":
            subtract(exp_arr)
            continue
        elif exp_arr[1] in "/":
            divide(exp_arr)
            continue
        elif exp_arr[1] in "*":
            multiply(exp_arr)
            continue
