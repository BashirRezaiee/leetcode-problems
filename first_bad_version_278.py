# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after 
# a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. 
# Implement a function to find the first bad version. You should minimize the number of 
# calls to the API.


# Fake API (return all values from 3 to 10 as bad version)
def isBadVersion(version):
    return True if version in range(3, 10) else False

def firstBadVersion(n: int) -> int:
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            right = mid

        else: 
            left = mid + 1

    return left # we can return either right or left 

# Test
n = 5
print(firstBadVersion(n)) # 3

# Explaination
# [1, 2, 3 ,4 ,5]
#  L     M     R   ====> M is bad, so R = M
#  L  M  R         ====> M is good, so L = M + 1
#        L         ====> R and L is equal, so you can return R or L