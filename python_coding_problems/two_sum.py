# Problem:
# Given an array of integers nums and an integer target, find the indices of two numbers whose sum equals the target.

# Example
# nums = [2, 7, 11, 15]
# target = 9

# 2 + 7 = 9

# So the answer is:

# [0, 1]

# because nums[0] + nums[1] = 9.

def two_sum(nums: list, target: int):
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        else:
            seen[num] = index
    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
