//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int dp[201][201][2];
    int countWays(int n, string s)
    {
        memset(dp,-1,sizeof(dp));
        mem(s,0,n-1,true);
    }
    int mem(string &s,int i,int j,bool istrue)
    {
        if(i>j)
          return 0;
        
        if(dp[i][j][istrue]!=-1)
          return dp[i][j][istrue];
        if(i==j)
        {
            if(istrue==true)
              return s[i]=='T';
            else
              return s[i]=='F';
            // return dp[i][j][istrue];
        }
        int ans=0;
        for(int k=i+1;k<j;k+=2)
        {
            int lt=mem(s,i,k-1,true);
            int rt=mem(s,k+1,j,true);
            int lf=mem(s,i,k-1,false);
            int rf=mem(s,k+1,j,false);
            if(s[k]=='|')
            {
                if(istrue==true)
                  ans+=lt*rt+lt*rf+lf*rt;
                else
                  ans+=lf*rf;
            }
            else if(s[k]=='&')
            {
                if(istrue==true)
                  ans+=rt*lt;
                else
                  ans+=rf*lf+rt*lf+lt*rf;
            }
            else if(s[k]=='^')
            {
                if(istrue==true)
                  ans+=lt*rf+lf*rt;
                else
                  ans+=lt*rt+lf*rf;
            }
        }
        return dp[i][j][istrue]=ans%1003;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string s;
        cin>>s;
        
        Solution ob;
        cout<<ob.countWays(n, s)<<"\n";
    }
    return 0;
}
// } Driver Code Ends