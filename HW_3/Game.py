# Kristin Schaefer
# CS325
# HW3, P2


# Bottom up approach for 'Game'. Returns True if A wins and False if A loses.
def game_bottomup(N):

    # make an array of length N + 1 to hold solutions
    # True = A wins, False = A loses
    game_result = [False] * (N+1)

    # fill array bottom up with solutions
    for n in range(2, N+1):
        game_result[n] = not(game_result[n-1])

    return game_result[n]


# Helper function for game_topdown().
def game_topdown_helper(N, topdown_memo):

    # Use value if calculated
    if N in topdown_memo:
        return topdown_memo[N]

    topdown_memo[N] = not(game_topdown_helper(N - 1, topdown_memo))

    return topdown_memo[N]


# Top down approach for 'Game'. Returns True if A wins and False if A loses.
def game_topdown(N):
    # Fill 0 with arbitrary False value
    # Fill base case 1 with False value
    topdown_memo = {0: False, 1: False}
    return game_topdown_helper(N, topdown_memo)


if __name__ == "__main__":

    print("2:", game_bottomup(2))
    print("3:", game_bottomup(3))
    print("4:", game_bottomup(4))
    print("5:", game_bottomup(5))
    print("6:", game_bottomup(6))
    print("7:", game_bottomup(7))
    print("8:", game_bottomup(8))
    print("9:", game_bottomup(9))

    print("2:", game_topdown(2))
    print("3:", game_topdown(3))
    print("4:", game_topdown(4))
    print("5:", game_topdown(5))
    print("6:", game_topdown(6))
    print("7:", game_topdown(7))
    print("8:", game_topdown(8))
    print("9:", game_topdown(9))