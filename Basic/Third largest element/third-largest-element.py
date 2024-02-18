class Solution:
    def thirdLargest(self,a, n):
        a.sort(reverse=True)
        for i in range(n):
            return a[2]
        return -1



#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr, n))
# } Driver Code Ends