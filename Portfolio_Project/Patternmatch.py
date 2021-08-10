# Kristin Schaefer
# CS325
# Portfolio Project, Problem B
# Sources:
# https://leetcode.com/problems/wildcard-matching/solution/
# https://stackoverflow.com/questions/49695477/removing-specific-duplicated-characters-from-a-string-in-python


def remove_dup_char(p, to_remove):
    if p == '':
        return p
    p1 = p
    # remove duplicates of specified char to_remove
    return "".join(p1[i] for i in range(len(p1)) if
                   i == 0 or not (p1[i - 1] == p1[i] and p1[i] in to_remove))


def patternmatch(string, p):
    # remove any duplicate * from pattern
    pattern = remove_dup_char(p, '*')
    # memo to store calculated values
    m = len(string)
    n = len(pattern)
    memo = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # process bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if the entire pattern is *, then True
            if pattern[0:] == '*':
                return True
            # remaining string & pattern match, or remaining pattern is *
            elif string[:i - 1] == pattern[:j - 1] or pattern[j:] == '*':
                memo[i][j] = True
            # if 1st char of string & pattern equal, keep processing remainder
            # patternmatch[string-1, p-1] or patternmatch[string-1, p-1]
            elif string[i - 1] == pattern[j - 1] or pattern[j - 1] == '?':
                if i == 1 and j == 1:
                    memo[i][j] = True
                else:
                    memo[i][j] = memo[i - 1][j - 1]
            # patternmatch[string, p-1] or patternmatch[string-1, p]
            elif pattern[j - 1] == '*':
                memo[i][j] = memo[i][j - 1] or memo[i - 1][j]
            # if none of the cases apply, then there is no match
            else:
                memo[i][j] = False

    return memo[i][j]


if __name__ == "__main__":
    print(patternmatch('abcde', '*a?c***'))     # True
    print(patternmatch('abcde', '*'))           # True
    print(patternmatch('abcde', '*a?c*'))       # True
    print(patternmatch('abcde', 'ad'))          # False
    print(patternmatch('abcde', 'abcde'))       # True
    print(patternmatch('abc', '???'))           # True
    print(patternmatch('abc', '?bc'))           # True
    print(patternmatch('abc', '***'))           # True
    print(patternmatch('abc', '?de'))           # False
