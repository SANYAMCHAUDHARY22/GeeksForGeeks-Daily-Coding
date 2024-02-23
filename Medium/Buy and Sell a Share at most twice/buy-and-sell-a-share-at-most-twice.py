from typing import List


class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        
        arr=[0]*(n)
        maxi = price[-1]
        ans = 0 
        for i in range(n-1, -1 , -1):
            if price[i] >  maxi : 
                maxi = price[i]
                
            else : 
                ans= max(ans,maxi- price[i])
                arr[i]= ans 
              
        mini = price[0]
        ansi = 0 
        num=[0]*n
        for i in range(n):
            if price[i] < mini : 
                mini = price[i]
            else : 
                ansi = max(price[i]- mini, ansi )
                num[i]= ansi
            
        #print(arr, num)
        fans = max(num[-1], arr[0])
        for i in range(n-1):
            fans = max(fans , num[i]+ arr[i+1])
            
        return  fans

 




#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends