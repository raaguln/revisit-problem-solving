'''
1. Pure recursion

start=0, path=[]
├── "a" is palindrome → path=['a']
│   └── start=1
│       ├── "a" is palindrome → path=['a', 'a']
│       │   └── start=2
│       │       ├── "b" is palindrome → path=['a', 'a', 'b']
│       │       │   └── start=3 ✅ append ['a', 'a', 'b']
│       │       └── backtrack (pop 'b')
│       └── "ab" is NOT palindrome ❌ skip
│       └── backtrack (pop 'a')
├── "aa" is palindrome → path=['aa']
│   └── start=2
│       ├── "b" is palindrome → path=['aa', 'b']
│       │   └── start=3 ✅ append ['aa', 'b']
│       └── backtrack (pop 'b')
├── "aab" is NOT palindrome ❌ skip
└── backtrack (pop 'aa')
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                print(start, end, substring)
                if is_palindrome(substring):
                    path.append(substring)
                    print(path)
                    backtrack(end, path)
                    path.pop()
        
        backtrack(0, [])
        return res

'''
2. DP - most optimal
'''
