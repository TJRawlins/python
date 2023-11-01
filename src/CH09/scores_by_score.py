scores_file = r"c:/repos/Python/py3basics/DATA/testscores.dat"
scores = {}

with open(scores_file) as src_file:
    # content = src_file.read().splitlines()
    # print(content)
    for i, line in enumerate(src_file, 1):
        scores[line.split(':')[0]] = int(line.split(':')[1].strip('\n'))


for name, score in sorted(scores.items(), key=lambda e: (e[1]), reverse=True):
    if score <= 75:
        print(f"{name}'s grade is a F")
    elif score > 75 and score < 83:
        print(f"{name}'s grade is a D")
    elif score > 82 and score < 89:
        print(f"{name}'s grade is a C")
    elif score > 88 and score < 95:
        print(f"{name}'s grade is a B")
    elif score > 94:
        print(f"{name}'s grade is an A")

print(sum(scores.values()) / len(scores))