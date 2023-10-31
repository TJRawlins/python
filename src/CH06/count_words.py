import sys

alice_file = r"c:/repos/Python/py3basics/DATA/alice.txt"

for word in sys.argv[1:]:
    with open(alice_file) as src_file:
        contents = src_file.read()
        print(contents.lower().count(word.lower()))
