from math import floor, log, inf


def buildSuffixArray(S):
    suffixPosition = [ord(s)-96 for s in S]
    P = floor(log(len(S)))
    for i in forLoop(1, lambda i: i <= (1 << P), lambda i: i << 1):
        tuples, mx = buildTuples(suffixPosition, i)
        suffixPosition = radixSort(tuples, mx)

    sa = toSuffixString(suffixPosition, S)
    return sa


def buildCompressedSuffixArray(S):
    suffixPosition = [ord(s)-96 for s in S]
    P = floor(log(len(S)))
    for i in forLoop(1, lambda i: i <= (1 << P), lambda i: i << 1):
        tuples, mx = buildTuples(suffixPosition, i)
        suffixPosition = radixSort(tuples, mx)

    sa = toCompressedSuffix(suffixPosition, S)

    return sa


def buildTuples(substring, ln):
    substrings = []
    n = len(substring)
    mx = -inf
    for i in range(n):
        firstSubstring = substring[i]
        if (i + ln) < n:
            secondSubstring = substring[i+ln]
        else:
            secondSubstring = 0
        substrings.append(Substring((firstSubstring, secondSubstring), i))
        mx = max(mx, firstSubstring, secondSubstring)
    return substrings, mx


def radixSort(substrings, maxPos):
    firstDigitSorted = countingSort(substrings, digit=1, lenCounter=maxPos)
    secondDigitSorted = countingSort(
        firstDigitSorted, digit=0, lenCounter=maxPos)
    ans = normalizeTuples(secondDigitSorted)
    return ans


def countingSort(substrings, digit, lenCounter):
    counter = [0]*(lenCounter+1)
    for substring in substrings:
        counter[substring.tuple[digit]] += 1

    for i in range(1, lenCounter+1):
        counter[i] = counter[i] + counter[i-1]

    ans = [0]*len(substrings)
    counter = [0] + counter
    for substring in substrings:
        pos = counter[substring.tuple[digit]]
        ans[pos] = substring
        counter[substring.tuple[digit]] += 1
    return ans


def normalizeTuples(tuples):
    """
    Assign each Substring's index to its order position.
    [([1,0], 3), ([1,0], 0), ([1,2], 1), ([2,0], 2), ([2,3], 4)]
         0           1           2          3           4
    => [1, 2, 3, 1, 4]
    """
    ans = [0]*len(tuples)
    i = 1
    pos = 1
    new_val = tuples[0].tuple
    for i in range(len(ans)):
        if new_val != tuples[i].tuple:
            new_val = tuples[i].tuple
            pos += 1
        ans[tuples[i].index] = pos
    return ans


def toSuffixString(suffixPosition, str):
    sa = [0]*len(suffixPosition)
    for i in range(len(sa)):
        sa[suffixPosition[i]-1] = str[i:]
    return sa


def toCompressedSuffix(suffixPosition, str):
    sa = [0]*len(suffixPosition)
    for i in range(len(sa)):
        sa[suffixPosition[i]-1] = i
    return sa


def forLoop(start, condition, evolve):
    value = start
    while (condition(value)):
        yield value
        value = evolve(value)


def buildLCPArray(suffixArray, string):
    """
    suffixArray[rank] = S[i:]
    inv[S[i:]] = rank

    for compression purposes, S[i:] is replaced i.
    """
    n = len(string)
    inv = buildInvTable(suffixArray)
    LCPArray = [0]*n
    lcp = 0
    for i in range(len(string)):
        if inv[i] == n-1:
            lcp = 0
            continue
        j = suffixArray[inv[i]+1]
        while (i+lcp < n and j+lcp < n and string[i+lcp] == string[j+lcp]):
            lcp += 1

        LCPArray[inv[i]] = lcp

        if lcp > 0:
            lcp -= 1

    return LCPArray


def buildInvTable(suffixArray):
    inv = [0] * len(suffixArray)
    for i, s in enumerate(suffixArray):
        inv[s] = i
    return inv


class Substring:
    def __init__(self, t=tuple(), index=-1):
        self.tuple = t
        self.index = index

    def __str__(self):
        return "([{},{}],{})".format(self.tuple[0], self.tuple[1], self.index)

    def __repr__(self):
        return str(self)
