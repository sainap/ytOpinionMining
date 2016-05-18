with open('rep2016.txt') as f:
    lines = f.readlines()

for line in lines:
	if '(m-)' not in line:
		print line

