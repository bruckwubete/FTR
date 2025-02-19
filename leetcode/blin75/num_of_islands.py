from typing import List


class Solution:
    def dfs(self, i, j, grid):
        if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])) or grid[i][j] != '1':
            return False
        grid[i][j] = '0'
        #self.dfs(i - 1, j - 1, grid)
        self.dfs(i, j - 1, grid)
        #self.dfs(i + 1, j - 1, grid)

        self.dfs(i - 1, j, grid)
        self.dfs(i + 1, j, grid)

        #self.dfs(i - 1, j + 1, grid)
        self.dfs(i, j + 1, grid)
        #self.dfs(i + 1, j + 1, grid)
        return False

    def num_islands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(i, j, grid)
        return count


if __name__ == '__main__':
    s = Solution()
    ex1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(s.num_islands(ex1))
