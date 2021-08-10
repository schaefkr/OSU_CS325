# Kristin Schaefer
# CS325
# Portfolio Project, Problem C


def getTesla(maze):
    # check if maze is valid
    if len(maze) == 0:
        return 0

    # create a table to store results
    # mhp = minimum health pts, chp = current health pts
    mhp = [[0] * len(maze[0]) for i in range(len(maze))]
    chp = [[0] * len(maze[0]) for i in range(len(maze))]

    # fill mhp bottom-up
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            # base case is already filled
            if i == 0 and j == 0:
                # base case - prefill starting cell
                # negative step
                if maze[0][0] < 0:
                    mhp[0][0] = abs(maze[0][0]) + 1
                    chp[0][0] = maze[0][0] + mhp[0][0]
                # positive step
                else:
                    mhp[0][0] = 0
                    chp[0][0] = maze[0][0]
                continue

            # fill out of bounds cells with values
            mhp_left = mhp_above = float('inf')
            chp_left = chp_above = 0
            # if cell to left is valid
            if j != 0:
                mhp_left = mhp[i][j-1]
                chp_left = chp[i][j-1]
            # if cell above is valid
            if i != 0:
                mhp_above = mhp[i-1][j]
                chp_above = chp[i-1][j]

            # select best mhp from above or left cell
            # if mhp is equal, then choose cell with best chp
            mhp_prev = 0
            chp_prev = 0
            if mhp_above < mhp_left:
                mhp_prev = mhp_above
                chp_prev = chp_above
            elif mhp_above > mhp_left:
                mhp_prev = mhp_left
                chp_prev = chp_left
            elif mhp_above == mhp_left:
                if chp_above > chp_left:
                    mhp_prev = mhp_above
                    chp_prev = chp_above
                else:
                    mhp_prev = mhp_left
                    chp_prev = chp_left

            # negative step
            if maze[i][j] < 0:
                hp_cost = abs(maze[i][j])
                if chp_prev > hp_cost:
                    mhp[i][j] = mhp_prev
                    chp[i][j] = chp_prev - hp_cost
                else:
                    mhp[i][j] = mhp_prev + hp_cost
                    chp[i][j] = 1
            # positive step
            else:
                mhp[i][j] = mhp_prev
                chp[i][j] = chp_prev + maze[i][j]

    return mhp[len(maze)-1][len(maze[0])-1]


if __name__ == "__main__":
    # output: 2
    maze_1 = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
    print(getTesla(maze_1))
    # output: 4
    maze_2 = [[-1, -1, -3], [-50, -1, -5], [100, 5, -1]]
    print(getTesla(maze_2))
