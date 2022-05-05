# ====================== Problem =====================:


# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index where 
# it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# ====================== Solution =====================:


from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left


# ====================== Run =====================:


print(searchInsert([1, 3, 5, 7], 6)) # 3
print(searchInsert([1, 3, 5, 7], 8)) # 4


# ====================== Trace ===================:


# [1, 3, 5, 7]  t = 6
#  l  m     r  ===> m < t -> l = m + 1 == 2
#        lm r  ===> m < t -> l = m + 1 == 3
#           rlm ==> m > t -> r = m - 1 == 2 
#        rm l  ===> r < l loop breaks 
#
# return l because l always have the right value


# [1, 3, 5, 7] t = 8
#  l  m     r  ===> m < t -> l = m + 1 == 2
#        lm r  ===> m < t -> l = m + 1 == 3
#           rlm ==> m < t -> l = m + 1 == 4
#           rm l => r < l loop breaks

# return l 