# Problem statement

# Given a list containing N-1 distinct integers from 1 to N, find the missing number.

# Exactly one number is missing. The list may be unsorted.

# Example 1

# nums = [1, 2, 4, 5]
# N = 5

# Output: 3

def find_missing_number_from_1_to_n(nums: list, n: int):
    missing = []
    for num in range(1, n + 1):
        if num not in nums:
            return num
    return None

if __name__ == '__main__':
    nums =  [1, 2, 4, 5]
    n = 5
    print(find_missing_number_from_1_to_n(nums, n))
