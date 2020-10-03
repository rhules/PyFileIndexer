import os
import sys
from os.path import join
from typing import List

index = "..\\index"
if len(sys.argv) < 2:
    print("too few arguments! format is \"python indexer.py [directory path]\" or \"python indexer.py [directory path] [index file]")
    print("too few arguments! format is \"python indexer.py [directory path]\" or \"python indexer.py [directory "
          "path] [index file]")
    sys.exit()
elif len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = sys.argv[1]
    index = sys.argv[2]
with open(index, 'w', encoding='utf-8') as f:
    for root, dirs, files in os.walk(path):
        catch: List[str] = [".mkv", ".wmv", ".mp4", ".m4v", ".mov", ".avi"]
        for name in files:
            for o in catch:
                if str(name).endswith(o):
                    f.write(str(join(root, name) + "\n"))
f.closed
