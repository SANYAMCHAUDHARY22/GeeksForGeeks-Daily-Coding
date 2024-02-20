#User function Template for python3

#User function Template for python3

class Solution:
   
    def wordBreak(self, input_string, word_dict):
        def wordBreakUtil(s, word_dict):
            if not s:
                self.result = 1
                return
       
            temp, pos = "", 1
            for i in s:
                temp += i
                if temp in word_dict:
                    wordBreakUtil(s[pos:], word_dict)
                pos += 1
       
        self.result = 0
        wordBreakUtil(input_string, word_dict)
        return self.result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		ob = Solution()
		res = ob.wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends