# Kristin Schaefer
# CS325
# HW4, P1

# Sources
# https://stackoverflow.com/questions/4487438/maximum-sum-of-non-consecutive-elements


# Top down approach
def max_independent_set(nums):
    # call mis_helper to get top down results stored in a dictionary
    results = mis_helper(nums, len(nums)-1, {})
    # get solution from results of topdown_memo from mis_helper function
    solution = []
    n = len(results) - 1
    while n >= 0:
        if n < 1:
            solution.append(results[0])
            break
        if n == 1:
            solution.append(max(results[0], results[1]))
            break

        d1 = results[n] - results[n-1]
        d2 = results[n] - results[n-2]

        if d1 == 0 and d2 == 0:
            n -= 1
        elif d1 > d2:
            n -= 1
        else:
            solution.append(d2)
            n -= 2

    # reverse solution list and return
    solution.reverse()
    return solution


def mis_helper(nums, n, topdown_memo):
    # Use value if calculated
    if n in topdown_memo:
        return topdown_memo[n]

    # otherwise calculate value and store in topdown_memo
    if n < 0:
        return 0
    else:
        topdown_memo[n] = max(mis_helper(nums, n-1, topdown_memo), mis_helper(nums, n-2, topdown_memo) + nums[n])

    # check if topdown_memo is filled in
    # if it is, return topdown_memo
    # otherwise only return current result
    if n == len(nums) - 1:
        return topdown_memo
    else:
        return topdown_memo[n]


if __name__ == "__main__":

    print(max_independent_set([7, 2, 5, 8, 6])) #7, 5, 6
    print(max_independent_set([7, 5, -50, 8, 12, 2, 22])) #7, 12, 22