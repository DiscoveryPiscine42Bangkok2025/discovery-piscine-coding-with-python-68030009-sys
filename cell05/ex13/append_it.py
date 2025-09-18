import sys
import re

args sys.argv[1:]

if not args:
    print("none")
else:
    for word in args:
        if not re.search(r'isms', word):
            print (f"(word)ism")
