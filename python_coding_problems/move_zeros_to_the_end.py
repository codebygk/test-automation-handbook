# Problem Statement

# Given a list of integers, move all 0s to the end of the list while maintaining the relative order of the non-zero elements.

# Ideally, do this in-place without creating another list.

# Example

# Input:  [0, 1, 0, 3, 12]

# Output: [1, 3, 12, 0, 0]

def move_zeros_to_the_end(nums: list):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    print(move_zeros_to_the_end(nums))