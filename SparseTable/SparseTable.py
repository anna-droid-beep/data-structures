from math import floor, log, inf


def buildSparseTable(values, func):
    N = len(values)
    P = floor(log(N)/log(2))
    log2 = [0] * (N+1)
    dp = [[None for _ in range(N)] for _ in range(P+1)]
    it = [[None for _ in range(N)] for _ in range(P+1)]

    for j in range(2, N+1):
        log2[j] = log2[j//2] + 1

    for j in range(N):
        dp[0][j] = values[j]
        it[0][j] = j

    for i in range(1, P+1):
        for j in for_loop(0, lambda j: j + (1 << i) <= N, lambda j: j+1):
            left = dp[i-1][j]
            right = dp[i-1][j + (1 << (i-1))]
            dp[i][j] = func(left, right)
            if left <= right:
                it[i][j] = it[i-1][j]
            else:
                it[i][j] = it[i-1][j + (1 << (i-1))]

    return log2, dp, it


def for_loop(start, condition, evolve):
    value = start
    while (condition(value)):
        yield value
        value = evolve(value)


def rangeQuery(l, r, log2, dp, func):
    ln = r - l + 1
    p = log2[ln]
    left = dp[p][l]
    right = dp[p][r-(1 << p)+1]
    return func(left, right)


def minIndexRangeQuery(l, r, log2, it, dp):
    ln = r - l + 1
    p = log2[ln]
    left = dp[p][l]
    right = dp[p][r-(1 << p) + 1]
    if left < right:
        return it[p][l]
    else:
        return it[p][r-(1 << p)+1]


def cascadingQuery(l, r, log2, dp, func, initVal):
    val = initVal
    while (l <= r):
        p = log2[r-l+1]
        val = func(val, dp[p][l])
        l += (1 << p)
    return val


values = [4, 2, 3, 7, 1, 5, 3, 3, 9, 6, 7, -1, 4]
log2, dp, it = buildSparseTable(values, min)

for l, r, expected in [(0, 4, 1), (0, 0, 4), (1, 8, 1), (0, 3, 2), (0, 12, -1)]:
    ans = rangeQuery(l, r, log2, dp, min)
    ans2 = cascadingQuery(l, r, log2, dp, min, inf)
    print("Range Query: {} should be {}: {}".format(
        ans, expected, ans == expected))
    print("Cascading Query: {} should be {}: {}".format(
        ans2, expected, ans2 == expected))
