import sys

file_path = r"c:/repos/Python/py3basics/DATA/"

for file_name in sys.argv[1:]:
    with open(file_path + file_name) as filename:
        for i, strline in enumerate(filename,1):
            line = strline.strip()
            print(i, line)

