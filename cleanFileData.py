import sys
import re

res = []
for line in sys.stdin:
    line = line.strip()
    if line.startswith("#"):
        continue
    line = re.sub(r"\s+", '',line)
    line = re.sub(r",,", ",NA,", line)
    line = re.sub(r",$", ",NA", line)
    res.append(line)
print "\n".join(i for i in res)
