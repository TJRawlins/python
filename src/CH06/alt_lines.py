alt_file = r"c:/repos/Python/py3basics/DATA/alt.txt"
a = open("a.text", "w+")
b = open("b.text", "w+")

with open(alt_file) as src_file:
    for i, line in enumerate(src_file, 1):
        if line[0] == "a":
            a.write(line)
        elif line[0] == "b":
            b.write(line)

a.close()
b.close()