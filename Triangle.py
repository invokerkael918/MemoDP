class SolutionDFS:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        self.mini = sys.maxsize
        self.dfs(triangle, 0, 0, 0)
        return self.mini

    def dfs(self, triangle, x, y, path_num):
        if x == len(triangle):
            self.mini = min(path_num, self.mini)
            return
        self.dfs(triangle, x + 1, y, path_num + triangle[x][y])
        self.dfs(triangle, x + 1, y + 1, path_num + triangle[x][y])


class SolutionDivideConquer:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        return self.D_C(triangle, 0, 0)

    def D_C(self, triangle, x, y):
        if x == len(triangle):
            return 0

        left = self.D_C(triangle, x + 1, y)
        right = self.D_C(triangle, x + 1, y + 1)
        return min(left, right) + triangle[x][y]

class SolutionDP:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        return self.DP(triangle, 0, 0,{})

    def DP(self, triangle, x, y,memo):
        if x == len(triangle):
            return 0
        if (x,y) in memo:
            return memo[(x,y)]
        left = self.DP(triangle, x + 1, y,memo)
        right = self.DP(triangle, x + 1, y + 1,memo)

        memo[(x,y)] = min(left,right) + triangle[x][y]
        return memo[(x,y)]
