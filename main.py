def maxminPath(grid):

    def recDp(row, column, dp, grid, prev):
        numOfRow , numOfCol =  len(dp) , len(dp[0])

        if row >= numOfRow or column >= numOfCol:
            return

        elif row == 0 and column ==0:
            dp[0][0] = grid[0][0]

        elif dp[row][column] == 0:
            dp[row][column] = min(prev, grid[row][column])

        else:
            if row == numOfRow - 1 and column == numOfCol - 1:

                dp[row][column] = max(min(prev, grid[row][column]), dp[row][column])
                print(dp)

            else:
                dp[row][column] = min(prev,grid[row][column])

        recDp(row, column+1, dp, grid, dp[row][column])
        recDp(row+1, column, dp, grid, dp[row][column])

    numOfRow = len(grid)
    numOfCol = len(grid[0])

    dp = [[0 for i in range(numOfCol)] for j in range(numOfRow)]
    recDp(0,0,dp,grid,0)

    return dp[numOfRow-1][numOfCol-1]

if __name__ == "__main__":
    print(maxminPath([[8,6,3],[6,4,9]]))