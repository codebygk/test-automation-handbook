# Problem statement

# Given a list of integers, find the second-largest distinct element without using sorting.

# Example

# Input:
# nums = [10, 5, 8, 20, 15]

# Output:
# 15

def find_second_largest_element_without_sorting(nums: list):
    largest = nums[0]
    second_largest = nums[0]
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest

if __name__ == '__main__':
    nums = [10, 5, 8, 20, 15]
    print(find_second_largest_element_without_sorting(nums))