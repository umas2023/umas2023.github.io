class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1,n+1):
            minn = float('inf')
            for j in range(1,int(i**0.5)+1):
                minn = min(minn,dp[i-j*j])
            dp[i] = minn +1
        return dp[n]
    
print(Solution().numSquares(12))