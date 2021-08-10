# Kristin Schaefer
# CS325
# HW4, P2


def feedDog(hunger_level, biscuit_size):
    # sort both arrays
    hunger_level.sort()
    biscuit_size.sort()

    num_dogs = 0    # number of dogs that can be fed
    i = 0           # current dog
    j = 0           # current biscuit
    while (i < len(hunger_level)) and (j < len(biscuit_size)):
        if hunger_level[i] <= biscuit_size[j]:
            num_dogs += 1       # 1 dog has been fed
            i += 1              # go to next dog
            j += 1              # go to next biscuit
        else:
            j += 1              # go to next biscuit

    return num_dogs


if __name__ == "__main__":

    print(feedDog([1, 2, 3], [1, 1]))  # output: 1
    print(feedDog([1, 2], [1, 2, 3]))  # output: 2
    print(feedDog([4, 5, 6], [2, 3, 6]))  # output: 1

