import re
with open('./blocklist.xml') as f:
    for line in f.readlines():
        pattern_1 = r'blockID="i.+\d".+?\n|blockID="g.+\d".+?\n'
        if re.search(pattern_1, line):
            print(line)