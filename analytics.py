with open('rep2008.txt') as r:
    linesrep = r.readlines()

with open('dem2008.txt') as d:
    linesdem = d.readlines()

# [d, r, c+, c-, u+, u-, c- d, c- r]
totaldem = [0, 0, 0, 0, 0, 0]
totalrep = [0, 0, 0, 0, 0, 0]

alldem = 0
allrep = 0
for dline in linesdem:
	if len(dline) > 0:
		alldem = alldem + 1
		if '(d)' in dline:
			totaldem[0] = totaldem[0] + 1
		if '(r)' in dline:
			totaldem[1] = totaldem[1] + 1
		if '(c+)' in dline:
			totaldem[2] = totaldem[2] + 1
		if '(c-)' in dline:
			totaldem[3] = totaldem[3] + 1
		if '(u+)' in dline:
			totaldem[4] = totaldem[4] + 1	
		if '(u-)' in dline:
			totaldem[5] = totaldem[5] + 1	
							

for rline in linesrep:
	if len(rline) > 0:
		allrep = allrep + 1
		if '(d)' in rline:
			totalrep[0] = totalrep[0] + 1
		if '(r)' in rline:
			totalrep[1] = totalrep[1] + 1
		if '(c+)' in rline:
			totalrep[2] = totalrep[2] + 1
		if '(c-)' in rline:
			totalrep[3] = totalrep[3] + 1
		if '(u+)' in rline:
			totalrep[4] = totalrep[4] + 1	
		if '(u-)' in rline:
			totalrep[5] = totalrep[5] + 1	



totalrep[:] = [x * 100 / allrep for x in totalrep]
totaldem[:] = [x * 100 / alldem for x in totaldem]

print "alldem is " + str(alldem) + ", allrep is " + str(allrep)
print totalrep
print totaldem



# key [d, r, c+, c-, u+, u-]

# 2016 
# alldem is 105, allrep is 185
# rep : [2, 19, 15, 31, 11, 17]
# dem : [13, 2, 19, 39, 5, 20]

# 2012 
# alldem is 138, allrep is 154
# rep : [1, 27, 20, 23, 7, 12]
# dem : [18, 4, 18, 42, 1, 37]

# 2008
# alldem is 91, allrep is 42
# rep : [7, 30, 9, 9, 4, 4]
# dem : [18, 4, 24, 30, 3, 15]


