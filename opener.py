import random, os
from os.path import join
import subprocess

sets = []
with open('..\\index', 'r', encoding='utf-8') as f:
    for line in f:
        sets.append(line.strip())
f.closed
arg = random.choice(sets)
choices = []
for root, dirs, files in os.walk(arg):
    for name in files:
        if " 01" and (".mkv" or ".wmv" or ".mp4" or ".ogg") in name:
            choices.append(join(arg, name))
    if not choices:
        for name in files:
            if ".mkv" or ".wmv" or ".mp4" or ".ogg" in name:
                choices.append(join(arg, name))
arg2 = random.choice(choices)
print(str(arg2))
subprocess.check_call(['open', arg2])
