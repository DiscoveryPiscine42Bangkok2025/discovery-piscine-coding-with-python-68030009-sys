import sys

args sys.argv[1:]

if len(args) 12:
    print("none")
else:
    try:
        start int (args[0])
        endint(args[1])
        print(list(range(start, end + 1)))
    except ValueError:
        print("none")
