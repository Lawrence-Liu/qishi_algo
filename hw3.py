#934
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        #initialize first island
        n = len(A)
        m = len(A[0])
        visited = [[False for i in range(n)] for j in range(m)]
        first_point = (-1,-1)
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    first_point = (i,j)
                    break
            if first_point != (-1,-1):
                break
        visited[first_point[0]][first_point[1]] = True
        island = [first_point]
        this_level = [first_point]
        
        
        while this_level:
            next_level = []
            for x in this_level:
                if (x[0] -1) > -1 and A[x[0]-1][x[1]] == 1 and not visited[x[0]-1][x[1]]:
                    next_level.append((x[0]-1, x[1]))
                    visited[x[0]-1][x[1]] = True
                if (x[0] +1) < n and A[x[0]+1][x[1]] == 1 and not visited[x[0]+1][x[1]]:
                    next_level.append((x[0]+1, x[1]))
                    visited[x[0]+1][x[1]] = True
                if (x[1] -1) > -1 and  A[x[0]][x[1]-1] == 1 and not visited[x[0]][x[1]-1]:
                    next_level.append((x[0], x[1]-1))
                    visited[x[0]][x[1]-1] = True
                if (x[1] + 1) < m and A[x[0]][x[1]+1] == 1 and not visited[x[0]][x[1]+1]:
                    next_level.append((x[0], x[1]+1))
                    visited[x[0]][x[1]+1] = True
            island += next_level
            this_level = next_level
        
        print('island:', island )
        this_level = island
        distance = 0
        flag = False
        
        while not flag:
            next_level = []
            print('this_level:', this_level)
            for x in this_level:
                if (x[0] -1) > -1 and not visited[x[0]-1][x[1]]:
                    if A[x[0]-1][x[1]] == 1:
                        flag = True
                        break
                    else:    
                        next_level.append((x[0]-1, x[1]))
                        visited[x[0]-1][x[1]] = True
                if (x[0] + 1) < n and not visited[x[0]+1][x[1]]:
                    if A[x[0]+1][x[1]] == 1:
                        flag = True
                        break
                    else:    
                        next_level.append((x[0]+1, x[1]))
                        visited[x[0]+1][x[1]] = True
                if (x[1] -1) > -1 and not visited[x[0]][x[1]-1]:
                    if A[x[0]][x[1]-1] == 1:
                        flag = True
                        break
                    else:    
                        next_level.append((x[0], x[1]-1))
                        visited[x[0]][x[1]-1] = True
                if (x[1] +1) < m and not visited[x[0]][x[1]+1]:
                    if A[x[0]][x[1]+1]== 1:
                        flag = True
                        break
                    else:    
                        next_level.append((x[0], x[1]+1))
                        visited[x[0]][x[1]+1] = True
            if flag:
                break
            this_level = next_level
            distance += 1
            
        return distance
                

#542
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        A = matrix
        n = len(A)
        m = len(A[0])
        cur_level = [(i,j) for i in range(n) for j in range(m) if A[i][j]==0]
        results = [[0 for _ in range(m)] for _ in range(n)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        distance = 0
        while cur_level:
            next_level = []
            for x in cur_level:
                visited[x[0]][x[1]] = True
                results[x[0]][x[1]] = distance
            for x in cur_level:
                if (x[0] -1) > -1 and not visited[x[0]-1][x[1]]:
                    next_level.append((x[0]-1, x[1]))
                    visited[x[0]-1][x[1]] = True
                if (x[0] +1) < n and not visited[x[0]+1][x[1]]:
                    next_level.append((x[0]+1, x[1]))
                    visited[x[0]+1][x[1]] = True
                if (x[1] -1) > -1  and not visited[x[0]][x[1]-1]:
                    next_level.append((x[0], x[1]-1))
                    visited[x[0]][x[1]-1] = True
                if (x[1] + 1) < m  and not visited[x[0]][x[1]+1]:
                    next_level.append((x[0], x[1]+1))
                    visited[x[0]][x[1]+1] = True
            cur_level = next_level
            distance +=1
        return results

#513

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def depth(root):
            if not root:
                return 0
            else:
                return 1 + max(depth(root.left), depth(root.right))
        
        n = depth(root)
        
        ans = []
        def dfs(root,i):
            if not root:
                return 
            else:
                if i == n :
                    ans.append(root.val)
                    return
                else:
                    dfs(root.left,i+1)
                    dfs(root.right,i+1)
        dfs(root,1)
        return ans[0]

#200
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        def dfs(r,c):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        num_island = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '0':
                    num_island += 1
                    dfs(i,j)
        
        return num_island


#127
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        m = len(wordList)
        L = len(beginWord)
        
        all_combo_dict = defaultdict(list)
        
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        
        visited = set(beginWord)
        
        cur_level = [beginWord]
        distance = 1
        while cur_level:
            next_level = []
            for x in cur_level:
                for i in range(L):
                    intermediate_word = x[:i] + "*" + x[i+1:]
                    for word in all_combo_dict[intermediate_word]:

                        if word == endWord:
                            return distance+1
                        if word not in visited:
                            next_level.append(word)
                            visited.add(word)
            distance +=1
            cur_level = next_level
        return 0
#129

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        paths = []
        def dfs(root, arr):
            if (root == None):
                return
            if (root.left == None) & (root.right == None):
                paths.append(arr + [root.val])
            if root.right != None:  
                dfs(root.right, arr + [root.val])
            if root.left != None:
                dfs(root.left, arr + [root.val])
        def array2num(arr):
            return sum([int(a) *(10 **(len(arr) - 1 - i))  for i,a in enumerate(arr)])
        dfs(root, [])
        return sum([ array2num(path) for path in paths])