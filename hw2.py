# leetcode 69
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        start = 0
        end = x
        while start < (end - 1):
            mid = (start +end) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                end = mid
            else: 
                start = mid
        
        return start

# leetcode 74
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [] or matrix == [[]]:
            return False
        nrow = len(matrix)
        ncol = len(matrix[0])
        start = 0 
        end = nrow * ncol - 1
        while start < end - 1:
            mid = (start + end) // 2
            x,y = divmod(mid,ncol)
            print('mid = ', mid)
            print('x = ', x, 'y=', y)
            if matrix[x][y % ncol] == target:
                return True
            elif matrix[x][y % ncol] < target:
                start = mid
            else:
                end = mid
        x,y = divmod(start,ncol)
        if matrix[x][y % ncol] == target:
            return True
        x,y = divmod(end,ncol)
        print(x,y)
        if matrix[x][y % ncol] == target:
            return True
        return False


#leetcode 33
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findrotateindex(nums):
            left = 0 
            right = len(nums) - 1
            if nums[left] < nums[right]:
                return 0
           
            while left < (right - 1):
                mid = (right + left) // 2
                if nums[mid] < nums[mid-1]:
                    return mid
                elif nums[left] < nums[mid]:
                    left = mid
                else:
                    right = mid
            return right
        
        
        
        def bs(nums, target):
            left = 0
            right = len(nums) - 1
           
            
            while left < (right - 1):
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] <target:
                    left = mid
                else:
                    right = mid
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1
        
        if len(nums) == 0:
            return -1
        
        
        index = findrotateindex(nums)

        if index == 0:
            return bs(nums, target)
        
        if nums[0] <= target:
            return bs(nums[:index], target)
        elif bs(nums[index:], target) != -1:
            return index + bs(nums[index:], target)
        else:
            return -1


#leetcode 278

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        
        while start < (end-1):
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
            
        if isBadVersion(start):
            return start
        else:
            return end


#leetcode 300

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1]
        for i in range(1, len(nums)):
            lis = [dp[j] + 1 if nums[i] > nums[j] else 1 for j in range(i)]
            dp.append(max(lis))
        return max(dp)