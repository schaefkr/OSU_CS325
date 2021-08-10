# Kristin Schaefer
# CS325
# HW4, P2

import copy


def powerset_helper(pointer, choices_made, input, result):

    if pointer < 0:
        result.append(copy.deepcopy(choices_made))
        return

    choices_made.append(input[pointer])
    powerset_helper(pointer-1, choices_made, input, result)

    #backtracking
    choices_made.pop()  #remove last element added to choices_made
    powerset_helper(pointer - 1, choices_made, input, result)


def powerset(input):
    result = []
    powerset_helper(len(input)-1, [], input, result)
    return result


if __name__ == "__main__":

    print(powerset([1, 2, 3, 4]))