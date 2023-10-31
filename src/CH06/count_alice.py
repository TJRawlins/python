alice_file = r"c:/repos/Python/py3basics/DATA/alice.txt"

with open(alice_file) as src_file:
    contents = src_file.read()
    print(contents.count("Alice"))
