import sys
args = sys.argv

def main(a, b):
    print(compareValue(a, b))

def compareValue(a, b):
    if a >= b:
        return a
    elif b > a:
        return b

main(args[1], args[2])