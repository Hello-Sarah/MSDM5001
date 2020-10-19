import re
with open('./blocklist.xml') as f:
    for line in f.readlines():
        pattern_2 = r'id=\"[a-zA-Z0-9._-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+\"'
        if re.search(pattern_2, line):
            print(line)