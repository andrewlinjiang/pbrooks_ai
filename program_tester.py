#! /usr/bin/python3
import sys
res =[]

with open(sys.argv[1], 'r') as fp:
	content = fp.read().split('\n')
	line = content[int(sys.argv[3])].split(",")

for i in line:
	if i.isdigit():
		res.append(str(i))
with open(sys.argv[2], 'w') as op:
	op.write(",".join(res))
		