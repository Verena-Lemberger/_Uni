import subprocess
import json
import csv
import os
import re

cwd = os.path.dirname(os.path.realpath(__file__))

# get git logs from repository
output = subprocess.check_output([
    "git",
    "--no-pager",
    "log",
    "--pretty=%H %ct <%an> <%ae> <%s>"
], cwd=r"/Users/saschametzger/Projects/_Uni/Softwareentwicklung/tkinter-examples")

# format the logs
regex = "([0-9a-f]{40}) ([0-9]{10}) (<(.*?)>) (<(.*?)>) (<(.*?)>)"
reOutput = re.findall(regex, str(output))
matches = []
for match in reOutput:
    matches.append({"hash": match[0], "timestamp": match[1],
                    "author": match[2], "email": match[3], "subject": match[4]})

# create a json string from the matches
matches = json.dumps(matches)

# # write to .txt file
file = open(cwd + "/gitlog.txt", "w")
file.write(matches)
file.close()

# read the txt file and split the file by ; into lines
file = open(cwd + "/gitlog.txt", "r")
file_contents = json.loads(file.read())

# using a for loop to iterate over each row and save it to a csv file
with open(cwd + "/gitlog.csv", mode='w') as gitlog_csv:
    writer = csv.writer(gitlog_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["hash", "timestamp", "author", "email", "subject"])
    for line in file_contents:
        row = [line.get("hash"), line.get("timestamp"), line.get("author"), line.get("email"), line.get("subject")]
        writer.writerow(row)
        
# Closing files
file.close()
