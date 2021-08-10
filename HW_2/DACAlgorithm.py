# Kristin Schaefer
# CS325
# HW2, P3

# Sources
#https://stackoverflow.com/questions/57789350/divide-and-conquer-find-the-majority-of-element-in-array#57789505
#https://github.com/antmarakis/Algorithms/blob/master/Divide%20and%20Conquer/FindMajorityElement.py
#http://users.eecs.northwestern.edu/~dda902/336/hw4-sol.pdf
#http://anh.cs.luc.edu/363/handouts/MajorityProblem.pdf


# Helper function which takes an array of integers (days) and returns the count
# of the specified integer (day_index) to search for.
def GetCount(days, day_index):
    sum = 0
    for day in days:
        if day == day_index:
            sum += 1
    return sum


# Takes an array of integers from 1-7, where Monday = 1 and Sunday = 7,
# sorts the list of integers using divide and conquer technique,
# and returns the integer which has the most common frequency.
# If no majority is found, then the function returns None.
def MajorityBirthdays(days):
    n = len(days)

    if n == 1:
        return days[0]
    m = n // 2

    days_left = MajorityBirthdays(days[:m])
    days_right = MajorityBirthdays(days[m:])
    if days_left == days_right:
        return days_left

    left_count = GetCount(days, days_left)
    right_count = GetCount(days, days_right)

    if left_count > m:
        return days_left
    elif right_count > m:
        return days_right
    else:
        return None


if __name__ == "__main__":

    bdays1 = [3, 2, 3]
    print(MajorityBirthdays(bdays1))

    bdays2 = [2, 2, 1, 1, 1, 2, 2]
    print(MajorityBirthdays(bdays2))