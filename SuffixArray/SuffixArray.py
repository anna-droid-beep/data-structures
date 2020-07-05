class Substring:
    def __init__(self, tuple=tuple(), index=-1):
        self.tuple = tuple
        self.index = index

    def __str__(self):
        return "([{},{}],{})".format(self.tuple[0], self.tuple[1], self.index)

    def __repr__(self):
        return str(self)


def buildSuffixArray(S):
    nums = [ord(s)-96 for s in S]


def buildTuples(substring, ln):
    substrings = []
    n = len(substring)
    for i in range(n):
        firstSubstring = substring[i]
        if i + ln < n:
            secondSubstring = substring[i+ln]
        else:
            secondSubstring = 0
        substrings.append(Substring((firstSubstring, secondSubstring), i))
    return substrings


def countingSort(substrings, digit):
    counter = [0]*27
    for substring in substrings:
        counter[substring.tuple[digit]] += 1

    for i in range(1, 27):
        counter[i] = counter[i] + counter[i-1]

    ans = [0]*len(substrings)
    counter = [0] + counter
    for substring in substrings:
        pos = counter[substring.tuple[digit]]
        ans[pos] = substring
        counter[substring.tuple[digit]] += 1
    return ans


def radixSort(substrings):
    firstDigitSorted = countingSort(substrings, digit=1)
    secondDigitSorted = countingSort(firstDigitSorted, digit=0)
    ans = [0]*len(secondDigitSorted)
    i = 1
    pos = 0
    new_val = secondDigitSorted[0].tuple
    for i in range(len(ans)):
        if new_val != secondDigitSorted[i].tuple:
            new_val = secondDigitSorted[i].tuple
            pos += 1
        ans[secondDigitSorted[i].index] = pos
    return ans


init = [4, 3, 2, 1, 1, 2, 1, 2, 1]
res = buildTuples(init, 1)
print(res)
res = radixSort(res)
print(res)
res = buildTuples(res, 2)
print(res)
res = radixSort(res)
print(res)
res = buildTuples(res, 4)
print(res)
res = radixSort(res)
print(res)
