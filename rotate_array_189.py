# ==================== Problem ===================


# Given an array, rotate the array to the right by k steps, where k is non-negative.


# ==================== Solution ===================


from typing import List

def rotate(nums: List[int], k: int) -> None:

    # if k > len(nums)

    # k = 2 , len(nums) = 1
    # 2 % 1 = 0 ==> k = 0

    # k = 3 , len(nums) = 7
    # 3 % 7 = 3 ==> k = 3

    # k = 9, len(nums) = 7
    # 9 % 7 = 2 ==> k = 2

    k = k % len(nums)
    
    def reverse(nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp

            end -= 1
            start += 1
    
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums) - 1)

    print(nums)


# ====================== Run =====================


nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)


# ====================== Trace ===================


# [1, 2, 3, 4, 5, 6, 7]  reverse entire array
# [7, 6, 5, 4, 3, 2, 1]  reverse first k elements
# [5, 6, 7, 4, 3, 2, 1]  reverse other elements
# [5, 6, 7, 1, 2, 3, 4]
#   
