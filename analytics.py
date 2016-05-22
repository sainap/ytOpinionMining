def getFile(fileName):
    with open(fileName) as r:
        return r.readlines()

# [d, r, c+, c-, u+, u-, c- & d, c- & r, u- & d, u- & r, m-, m+]
def getStats(lines):
    stats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = 0
    for line in lines:
        if len(line) > 0:
            counter += 1
        if '(d)' in line:
            stats[0] = stats[0] + 1
        if '(r)' in line:
            stats[1] = stats[1] + 1
        if '(c+)' in line:
            stats[2] = stats[2] + 1
        if '(c-)' in line:
            stats[3] = stats[3] + 1
            if '(d)' in line:
                stats[6] += 1
            elif '(r)' in line:
                stats[7] += 1
        if '(u+)' in line:
            stats[4] = stats[4] + 1   
        if '(u-)' in line:
            stats[5] = stats[5] + 1
            if '(d)' in line:
                stats[8] += 1
            elif '(r)' in line:
                stats[9] += 1
        if '(m-)' in line:
            stats[10] += 1
        if '(m+)' in line:
            stats[11] += 1

    return [x * 100 / counter for x in stats]


# top-comment-stats = [r, d, r c-, r c+, d c-, d c+]
# [(top comment: [array of replies]])]
# commentstats = []

def processThread(fileName):
    # get the top comment
    topStats = {"(r)" : [], }
    commentthread = {}
    lines = getFile(fileName)
    for i in range(0, len(lines) - 1):
        line = lines[i]
        if len(line) > 0 and not line.startswith(' '):
            nextLine = lines[i + 1]
            replies = []
            counter = i + 1
            while nextLine.startswith('\t'):
                replies.append(nextLine)
                counter += 1
                nextLine = lines[counter]
            if len(replies) > 0:
                commentthread[line] = replies

    return commentthread
    for topComment in commentthread:
        if '(r)' in topComment:
            if '(c-)' in topComment
                # update (r)(c-)
            elif '(c-)' in topComment
                # update (r)(c+)
            else # update (r)


        currThread = commentthread[topComment]
        for reply in currThread:
            if 
                
print processThread("dem2012.txt")



    # collect all replies and store in array
    # process the array and update values


newrep = getStats(getFile("dem2016.txt"))


s =  "  dflkjlkaj"
print s.startswith(' ')




print type(getFile("rep2008.txt"))



