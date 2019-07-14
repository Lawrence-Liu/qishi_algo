# 518
class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
               if  j >= i:
                   dp[j] += dp[j - i]
        return dp[amount]

# 63
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        
        
        path_matrix = [ [0] * (n+1) for i in range(m+1)]
        
        
        for i in range(m-1,-1, -1):
            for j in range(n-1, -1, -1):
                
                if obstacleGrid[i][j] ==1:
                    path_matrix[i][j] = 0
                elif (i == m-1) & (j == n-1):
                    path_matrix[m-1][n-1] = 1
                else:
                    path_matrix[i][j] = path_matrix[i+1][j] + path_matrix[i][j+1]
        
        return path_matrix[0][0]

#5
class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return ''
        ans = [[0] *n for i in range(n)]
        ans[0][0] = 1
        max_len = 1
        left, right = 0,0
        for i in range(n):
            for j in range(0,i+1):
                if j == 0:
                    ans[i][j] = 1
                elif j == 1:
                    ans[i][j] = 1 if s[n-1-i] == s[n-i] else 0
                else:
                    ans[i][j] = ans[i-1][j-2] if s[n-1-i] == s[n-1-i+j] else 0
                if ans[i][j] == 1 and j >= max_len:
                    max_len = j
                    left, right = n - i - 1, n- 1 - i + j
                    
                    
        return s[left:(right + 1)]

#64
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        result = [[0] * len(grid[0]) for i in range(len(grid))] 
    
        #initialization
        result[0][0] = grid[0][0]
        
        for k in range(1,len(grid[0])):
            result[0][k] = result[0][k-1] + grid[0][k]
        for k in range(1, len(grid)):
            result[k][0] = result[k-1][0] + grid[k][0]
        for i in range(1, len(grid)): 
            for j in range(1,len(grid[0])):
                result[i][j] = min(result[i-1][j], result[i][j-1]) + grid[i][j]
                
            
        return result[-1][-1]
