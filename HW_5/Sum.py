# Kristin Schaefer
# CS325
# HW4, P1

from copy import deepcopy


def combination_helper(n, k, start, result, remainder, combination):
    if len(combination) == k+1:
        return # combination length exceeded k
    if (remainder == 0):
            if (len(combination) == k):
                result.append(deepcopy(combination))
            return # if len != k, then combination will be too short so just return
    elif (remainder < 0):
        return # sum exceeded the target

    for i in range(start, len(n)-k):
        combination.append(n[i])
        combination_helper(n, k, i+1, result, remainder-n[i], combination)
        #backtrack
        combination.pop()


def combination(n, k):
    result = []

    # make arr of ints in ascending order from 1-n or 1-9 if n > 9
    n_arr = [x for x in range(1, max(n+1, 10))]

    combination_helper(n_arr, k, 0, result, n, [])
    print(result)


if __name__ == "__main__":

    combination(6, 3) # [[1,2,3]]
    combination(9, 3) # [[1,2,6], [1,3,5], [2,3,4]]
