# Problem statement

# Given two lists of integers, find all elements that appear in both lists.

# Return each common element only once, preserving the order in which it first appears in the first list.

# Example 1
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [3, 4, 5, 6, 7]

# Output: [3, 4, 5]

def find_common_elements_between_two_lists(nums1: list, nums2: list):
    common_nums = []
    for num in nums1:
        if num in nums2 and num not in common_nums:
            common_nums.append(num)
    return common_nums

if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5, 3]
    nums2 = [3, 4, 5, 6, 7, 3]
    print(find_common_elements_between_two_lists(nums1, nums2))