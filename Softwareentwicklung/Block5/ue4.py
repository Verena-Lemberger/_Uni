import re

regex = r"a(bc|d*)a*"

test_str = ("abca \n"
	"ada \n"
	"abcddda \n"
	"abddda\n"
	"abdaaa")

matches = re.finditer(regex, test_str, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

