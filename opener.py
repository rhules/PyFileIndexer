import random, os
from os.path import join
import subprocess
from typing import List
import sys

sets = []
index = "..\\index"
if len(sys.argv) < 2:
    print("too few arguments! format is \"python opener.py [index file]\" or \"python opener.py [index file] [argument]")
else:
    index = sys.argv[1]
with open(index, 'r', encoding='utf-8') as f:
    for line in f:
        sets.append(line.strip())
f.closed
arg = ""
if len(sys.argv) > 2:
    term = sys.argv[2]
    options = []
    for name in sets:
        file = name.split("\\")
        if term in file[len(file)-1]:
            options.append(name)
    if options:
        arg = random.choice(options)
    else:
        print("no files found")
        sys.exit()
else:
    arg = random.choice(sets)
#for name in files:
#    if any(o in str(name) for o in catch):
#        if " 01" in str(name):
#            choices.append(join(root, name))
#if not choices:
#    for name in files:
#        if any(o in str(name) for o in catch):
#            choices.append(join(root, name))
#if not choices:
#    print("no valid options")
#else:
#arg2 = random.choice(choices)
sys.stdout.buffer.write(str(arg).encode('utf8'))
#subprocess.run(['open', arg2], check=True)
os.startfile(arg, 'open')
