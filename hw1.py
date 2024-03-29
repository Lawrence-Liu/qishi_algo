#leetcode 783

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        def preorder(root):
            if not root:
                return []
            return preorder(root.left) +  [root.val] + preorder(root.right)
        
        ordered_array = preorder(root)
        min_val = 1e5
        for i in range(0, len(ordered_array) - 1):
            diff = ordered_array[i+1] - ordered_array[i]
            min_val = min(diff, min_val)
        return min_val


#leetcode 544 

class Solution:
    def findContestMatch(self, n: int) -> str:
        arr = range(1,n+1)
        while n > 1:
            arr = ['(' + str(arr[i]) + ',' + str(arr[n-1-i]) + ')' for i in range(n//2)]
            n //= 2
        return arr[0]

#leetcode 247

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        table = {'1':'1','8':'8', '9':'6', '6':'9'}
        if n == 1:
            return ['0', '1','8']
        elif n == 2:
            return ["11","69","88","96"]
        
        else:
            temp = self.findStrobogrammatic(n-2)
            return [ j + x + table[j] for x in temp +  (list(set(['0' + x[1:-1] +'0' for  x in temp])) if n>3 else [])  for j in table]



#leetcode 698
class Solution:
     def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: 
            return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)