import random, os
from os.path import join
import subprocess
from typing import List
import sys

sets = []
index = "..\\index"
if len(sys.argv) < 2:
    print("too few arguments! format is \"python opener.py [index file]\" or \"python opener.py [index file] "
          "[arguments]")
else:
    index = sys.argv[1]
with open(index, 'r', encoding='utf-8') as f:
    for line in f:
        sets.append(line.strip())
f.closed
arg = ""
if len(sys.argv) > 2:
    term = sys.argv[2]
    fullPath = False
    exclusion = False
    if term == "fullpath" and len(sys.argv) > 3:
        term = sys.argv[3]
        fullPath = True
    options = []
    if term.startswith("-"):
        term = term[1:]
        exclusion = True
    for name in sets:
        if fullPath:
            if exclusion:
                if term not in str(name):
                    options.append(name)
            elif term in str(name):
                options.append(name)
        else:
            file = name.split("\\")
            if exclusion:
                if term not in file[len(file) -1 ]:
                    options.append(name)
            if term in file[len(file) - 1]:
                options.append(name)
    if options:
        arg = random.choice(options)
    else:
        print("no matching files found")
        sys.exit()
else:
    if sets:
        arg = random.choice(sets)
    else:
        print("no files found")
        sys.exit()
sys.stdout.buffer.write(str(arg).encode('utf8'))
os.startfile(arg, 'open')
