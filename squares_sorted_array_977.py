# ==================== Problem ===================

# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

# ==================== Solution ==================

from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        result = []
        
        while left <= right:
            l = nums[left] * nums[left]
            r = nums[right] * nums[right]

            if r > l:
                result.append(r)
                right -= 1
            else:
                result.append(l)
                left += 1
        
        return result[::-1]


# ===================== Run =====================


print(sortedSquares([-4, -1, 0, 3, 10])) # [0, 1, 9, 16, 100]    


# ==================== Trace ====================

# [-4, -1, 0, 3, 10]
#  L              R  ==> L*L < R*R ==> [100]
#  L          R      ==> L*L > R*R ==> [100, 16]
#       L     R      ==> L*L < R*R ==> [100, 16, 9]
#       L  R         ==> L*L > R*R ==> [100, 16, 9, 1]
#          RL        ==> L*L = R*R ==> [100, 16, 9, 1, 0]
#          R  L      ==> L > R     ==> loop breaks
# 
# reverse                          ==> [0, 1, 9, 16, 100]