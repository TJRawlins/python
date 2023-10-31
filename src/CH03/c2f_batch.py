import sys
# COMMAND LINE: python c2f_batch.py 100 0 -40

cstrs = sys.argv[1:] #1: means 1 parameter and any others
for cstr in cstrs:
    c = float(cstr)
    f = c * 9 / 5 + 32
    print(f"{c:.1f}c is {f:.1f}f")