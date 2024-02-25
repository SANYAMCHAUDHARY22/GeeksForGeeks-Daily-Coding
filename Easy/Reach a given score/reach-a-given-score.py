#User function Template for python3

class Solution:
    def count(self, n: int) -> int:
        #your code here
        
        dp = [0] * (n + 1)

        # There is one way to reach score 0 (no moves)
        dp[0] = 1
    
        # Iterate through possible moves
        for move in [3, 5, 10]:
            for i in range(move, n + 1):
                dp[i] += dp[i - move]
    
        return dp[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ob = Solution()
        print(ob.count(n))
        
# } Driver Code Ends