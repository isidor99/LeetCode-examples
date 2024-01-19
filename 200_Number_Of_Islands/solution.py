class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # get number of rows and columns
        rows = len(grid)
        cols = len(grid[0])
        
        # save information about visited nodes
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        result = 0

        
        # helper function which returns all node neighbors
        def neighbors(i, j):
            res = []
        
            # node neighbor can be node "above", "below", "left" or "right" to the given node
            if i > 0:
                res.append((i - 1, j))
            if i < rows - 1:
                res.append((i + 1, j))
            if j > 0:
                res.append((i, j - 1))
            if j < cols - 1:
                res.append((i, j + 1))
                
            return res


        # depth first search algorithm, iterative implementation
        def dfs(i, j):
            stack = [(i, j)]
            while len(stack) > 0:
                v = stack.pop()
                if visited[v[0]][v[1]] == False:
                    visited[v[0]][v[1]] = True
                    for k in neighbors(v[0], v[1]):
                        if grid[k[0]][k[1]] == '1' and visited[k[0]][k[1]] == False:
                            stack.append(k)

        # loop through all nodes and check if node value is 0, and if not was visited
        # if it wasn't visited, we found an island
        # then do depth first search starting from that node
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and visited[i][j] == False:
                    dfs(i, j)
                    result = result + 1

        # return result            
        return result
