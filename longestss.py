# "AABBEEDDDBBEE" -> {"D":3}
# 1. iterative


def longest(s):
    longestCh, currentCh = s[0] * 2
    longestLen, currentLen = [0] * 2

    for i in s:
        if i == currentCh:
            currentLen += 1
        else:
            currentCh = i
            currentLen = 1
        if currentLen >= longestLen:
            longestLen = currentLen
            longestCh = currentCh
    return {longestCh: longestLen}


print(longest("AABBEEDDDBBEE"))
