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




def processTopComment(tcomment, replies):
    result = [0] * 12
    for reply in replies:
        if '(r)' in reply:
            if '(u+)' in reply:
                result[0] += 1
            if '(u-)' in reply:
                result[1] += 1
            if '(c+)' in reply:
                result[2] += 1
            if '(c-)' in reply:
                result[3] += 1
        elif '(d)' in reply:
            if '(u+)' in reply:
                result[4] += 1
            if '(u-)' in reply:
                result[5] += 1
            if '(c+)' in reply:
                result[6] += 1
            if '(c-)' in reply:
                result[7] += 1
        else:
            if '(u+)' in reply:
                result[8] += 1
            if '(u-)' in reply:
                result[9] += 1
            if '(c+)' in reply:
                result[10] += 1
            if '(c-)' in reply:
                result[11] += 1
    if len(replies) != 0:
        result[:] = [x * 100.0 / len(replies) for x in result]

    return result


def processThread(fileName, repOrDem, attr):
    commentthread = {}
    lines = getFile(fileName)
    for i in range(0, len(lines) - 1):
        line = lines[i]
        if len(line) > 0 and not line.startswith(' ') \
            and i + 2 < len(lines):
            nextLine = lines[i + 1]
            replies = []
            counter = i + 1
            while nextLine.startswith('\t'):
                replies.append(nextLine)
                counter += 1
                nextLine = lines[counter]
            if len(replies) > 0:
                commentthread[line] = replies
    result = []
    for topComment in commentthread:
        if repOrDem in topComment and attr in topComment:
            result.append(processTopComment(topComment, commentthread[topComment]))

    concatenated = [0] * 12
    for index in range(12):
        total = 0
        for item in result:
            total += item[index]
        if len(result) > 0:
            concatenated[index] =  1.0 * total / len(result)
    return concatenated


# result of processThread is array of arrays where each array is as follows
# [(r u& +) (r & u-) (r & c+) (r & c-) (d & u+) (d & u-) (d & c+) (d & c-) (u+) (u-) (c+) (c-)]

print processThread("rep2008.txt", '(r)', '(c-)')
print processThread("rep2008.txt", '(r)', '(c+)')
print processThread("rep2008.txt", '(d)', '(c-)')
print processThread("rep2008.txt", '(d)', '(c+)')

print processThread("dem2008.txt", '(r)', '(c-)')
print processThread("dem2008.txt", '(r)', '(c+)')
print processThread("dem2008.txt", '(d)', '(c-)')
print processThread("dem2008.txt", '(d)', '(c+)')

print processThread("rep2012.txt", '(r)', '(c-)')
print processThread("rep2012.txt", '(r)', '(c+)')
print processThread("rep2012.txt", '(d)', '(c-)')
print processThread("rep2012.txt", '(d)', '(c+)')

print processThread("dem2012.txt", '(r)', '(c-)')
print processThread("dem2012.txt", '(r)', '(c+)')
print processThread("dem2012.txt", '(d)', '(c-)')
print processThread("dem2012.txt", '(d)', '(c+)')

print processThread("rep2016.txt", '(r)', '(c-)')
print processThread("rep2016.txt", '(r)', '(c+)')
print processThread("rep2016.txt", '(d)', '(c-)')
print processThread("rep2016.txt", '(d)', '(c+)')

print processThread("dem2016.txt", '(r)', '(c-)')
print processThread("dem2016.txt", '(r)', '(c+)')
print processThread("dem2016.txt", '(d)', '(c-)')
print processThread("dem2016.txt", '(d)', '(c+)')



    # collect all replies and store in array
    # process the array and update values









