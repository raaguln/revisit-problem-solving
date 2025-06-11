'''
https://leetcode.com/problems/decode-ways/

Time - O(2^n)
- At each index, the function may make up to two recursive calls:
  - One for single-digit decoding
  - One for valid two-digit decoding
- Total number of recursive calls grows exponentially with string length n

Space - O(n)
- Maximum recursion depth is n (length of the string)
- Each call adds one frame to the call stack
- No additional data structures used
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            # If we've reached the end, that's one valid decoding
            if i == len(s):
                return 1
            
            # If the current digit is '0', it can't be decoded
            if s[i] == '0':
                return 0
            
            # Take one digit
            res = dfs(i + 1)
            
            # Take two digits if valid (i.e., <= 26)
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                res += dfs(i + 2)
            
            return res

        return dfs(0)


'''
Bottom Up Optimized

Time - O(n)  
- Single pass from end to start of the string  
- Each position i is processed once  
- Constant time operations per index  
- Total time complexity is O(n)

Space - O(n)  
- 1D DP array of size n+1 to store ways to decode suffix s[i:]  
- No recursion stack used

Explanation -  
n - length of string s  
dp[i] - number of ways to decode substring s[i:]

DP logic -  
QUESTION -> How many ways can we decode s[i:]?

1. Base case:  
   - dp[n] = 1 (empty string has 1 decoding)

2. For i from n-1 down to 0:  
   - If s[i] == '0', no valid decoding → dp[i] = 0  
   - Else:  
     a) Take 1 digit → dp[i] += dp[i+1]  
     b) Take 2 digits (if 10 <= s[i:i+2] <= 26) → dp[i] += dp[i+2]  

Table - Step 0 after initialization →  
Let s = "226", n = 3  
dp = [?, ?, ?, 1] ← dp[3] = 1 (base case)  
Fill dp from right to left:

- i=2 → s[2]='6' → dp[2] = dp[3] = 1  
- i=1 → s[1]='2' + s[1:3]='26' → dp[1] = dp[2] + dp[3] = 1 + 1 = 2  
- i=0 → s[0]='2' + s[0:2]='22' → dp[0] = dp[1] + dp[2] = 2 + 1 = 3

Final result = dp[0] = 3
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] will represent number of ways to decode s[i:]
        dp = [0] * (n + 1)
        
        # Base case: empty string has 1 way to decode (do nothing)
        dp[n] = 1

        # Fill dp table from right to left
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                # Take one digit
                dp[i] = dp[i + 1]
                # Take two digits if valid
                if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                    dp[i] += dp[i + 2]

        return dp[0]
