#4

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            n, m = m, n
        
        if m == 0:
            if n % 2 ==0:
                return (nums2[n//2 - 1] + nums2[n//2])/2
            else:
                return nums2[(n-1)//2]
        
        if m== 1 and n == 1:
            return (nums1[0] + nums2[0]) / 2 
        
        set1 = (m + n + 1) // 2 
        
        lower = 0 
        upper = len(nums1) - 1
        
        
        i = (lower + upper) // 2
        j = set1 - i - 2
        
        
        while lower < upper - 1:
            
            if nums1[i+1] >= nums2[j] and nums2[j+1] >= nums1[i]:
                break
            elif nums1[i+1] > nums2[j]:
                lower = i
            else:
                upper = i
            i = (lower + upper) // 2
            j = set1 - i - 2
            
        
        if set1 == (m+n)/2:
            mid = (max(nums1[i], nums2[j]) + min(nums1[i+1] if i < (m-1) else 2e20, nums2[j+1] ))/2
        else:
            mid = max(nums1[i], nums2[j])
        return mid



#973
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = [point[0] ** 2 + point[1] **2  for point in points]
        
        idx = sorted(range(len(distance)), key=distance.__getitem__)
        
        return [points[i] for i in idx[0:K]]

#53
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(1,len(nums)):
                nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)

#215
 class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse = True)
        return nums[k-1]           
            