# Kristin Schaefer
# CS325
# HW3, P1

# Sources
# https://www.youtube.com/watch?v=5o-kdjv7FD0&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=2

# Description
def blockpuzzle_dp(N):
    # base case
    if N == 0 or N == 1:
        return 1
    # make an array of length N + 1 to hold solutions
    combinations = [0] * (N+1)
    # for loop to fill the combinations solutions array in bottom-up approach
    for i in range(0, N+1):
        if i == 0 or i == 1:
            combinations[i] = 1
        else:
            combinations[i] = combinations[i - 1] + combinations[i - 2]

    # return only the last result of the combinations array,
    # as this contains the final solution
    return combinations[N]


if __name__ == "__main__":

    print(blockpuzzle_dp(0))
    print(blockpuzzle_dp(1))
    print(blockpuzzle_dp(2))
    print(blockpuzzle_dp(3))
    print(blockpuzzle_dp(4))
    print(blockpuzzle_dp(5))