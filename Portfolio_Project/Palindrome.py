# Kristin Schaefer
# CS325
# Portfolio Project, Problem A Part 1 and Part 2
# Sources:
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-using-memoization/


def checkPalindrome_1_helper(s1, s2, m, n):
    # base case
    if m < 0 or n < 0:
        return 0

    # characters match
    elif s1[m] == s2[n]:
        return 1 + checkPalindrome_1_helper(s1, s2, m - 1, n - 1)

    # characters do not match
    else:
        return max(checkPalindrome_1_helper(s1, s2, m - 1, n),
                   checkPalindrome_1_helper(s1, s2, m, n - 1))


def checkPalindrome_1(string, k):
    # get length of max substring of split string
    m = n = len(string)
    max_substring = checkPalindrome_1_helper(string, string[::-1], m-1, n-1)

    if max_substring >= (n - k):
        return True
    else:
        return False


def checkPalindrome_2_helper(s1, s2, m, n, dp):
    # base case
    if m == 0 or n == 0:
        return 0

    # if sub problem is already stored
    if dp[m-1][n-1] != -1: return dp[m-1][n-1]

    # characters match
    if s1[m-1] == s2[n-1]:
        dp[m-1][n-1] = 1 + checkPalindrome_2_helper(s1, s2, m-1, n-1, dp)
        return dp[m-1][n-1]

    # characters do not match
    else:
        dp[m-1][n-1] = max(checkPalindrome_2_helper(s1, s2, m-1, n, dp), checkPalindrome_2_helper(s1, s2, m, n-1, dp))
        return dp[m-1][n-1]


def checkPalindrome_2(string, k):
    # create 2d array to store results
    m = n = len(string)
    dp = [[-1 for x in range(n+1)] for x in range(m+1)]

    # get length of max substring of split string
    max_substring = checkPalindrome_2_helper(string, string[::-1], m, n, dp)

    if max_substring >= (n - k):
        return True
    else:
        return False


if __name__ == "__main__":

    print(checkPalindrome_1('abcdcba', 1))      # True
    print(checkPalindrome_1('abcdeba', 2))      # True
    print(checkPalindrome_1('abcddeba', 2))     # True
    print(checkPalindrome_1('aaaaefbc', 4))     # True

    print(checkPalindrome_2('abcdcba', 1))      # True
    print(checkPalindrome_2('abcdeba', 2))      # True
    print(checkPalindrome_2('abcddeba', 2))     # True
    print(checkPalindrome_2('aaaaefbc', 4))     # True
