class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)
        
        
        dp = [[None]*(M+1) for i in range(N+1)]
        
        for i in range(N+1):
            for j in range(M+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[N][M]
                    
                    
                
        