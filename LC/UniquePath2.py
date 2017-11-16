class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for i in range(len(obstacleGrid[0])+1)] for j in range(len(obstacleGrid)+1)]
        dp[1][1] = 1
        for i in range(1,len(dp)):
            for j in range(1, len(dp[i])):
                if j == 1 and i == 1:
                    continue
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

list = [
  [0,0,0,0],
  [0,1,0,0],
  [0,0,0,0]
]

solu = Solution()
solu.uniquePathsWithObstacles(list)