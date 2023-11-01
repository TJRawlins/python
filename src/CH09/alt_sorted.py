alt_file = r"c:/repos/Python/py3basics/DATA/alt.txt"
a = open("a.text", "w+")
b = open("b.text", "w+")
alist = []
blist = []

with open(alt_file) as src_file:
    for i, line in enumerate(src_file, 1):
        if line[0] == "a":
            alist.append(line.strip('\n'))
        elif line[0] == "b":
            blist.append(line.strip('\n'))
    for i in sorted(alist, reverse=True):
        a.write(i + "\n")
    for i in sorted(blist):
        b.write(i + "\n")

a.close()
b.close()