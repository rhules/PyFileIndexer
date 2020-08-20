import random, os
from os.path import join
import subprocess
from typing import List

sets = []
with open('..\\index', 'r', encoding='utf-8') as f:
    for line in f:
        sets.append(line.strip())
f.closed
arg = random.choice(sets)
choices = []
for root, dirs, files in os.walk(arg):
    catch: List[str] = [".mkv", ".wmv", ".mp4", ".ogg", ".m4v"]
    for name in files:
        if any(o in str(name) for o in catch):
            if " 01" in str(name):
                choices.append(join(root, name))
    if not choices:
        for name in files:
            if any(o in str(name) for o in catch):
                choices.append(join(root, name))
if not choices:
    print("no valid options")
else:
    arg2 = random.choice(choices)
    print(str(arg2))
    #subprocess.run(['open', arg2], check=True)
    os.startfile(arg2, 'open')