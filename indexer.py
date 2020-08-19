import os
from os.path import join
with open('..\\index', 'w', encoding='utf-8') as f:
    #json.dump(os.walk('\\\\MYBOOKLIVE\\ryan\\Videos'), f)
    for root, dirs, files in os.walk('\\\\MYBOOKLIVE\\ryan\\Videos'):
        for name in dirs:
            f.write(str(join(root, name) + "\n"))
f.closed
