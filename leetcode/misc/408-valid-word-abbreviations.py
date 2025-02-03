'''
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        '''
        Substring - 
        1. continuous
        2. non-empty

        Invalid substitutions - 
        1. the numbers parsed are continuous (55 can't be 5 and 5)
        2. can't start with 0
        3. can't replace empty (0)

        Doubt - 
        1. -ve 
        2. Special characters
        3. caps / french letters

        Logic - 
        1. parse the abbr into characters and counts

        stringComponents = []
        - If char -> add to stringComponents
        - If digit -> take all digits and convert them to int

        2. accounting for the numbers in abbreviations, if the char (original and abbr) match up, then True
            Else False
        '''
        # TODO: Handle edge cases

        i = 0
        # for original string
        # index = 0
        parsedAbbr = []
        while i < len(abbr):
            # Numbers
            if abbr[i].isdigit():
                # Invalid 2 & 3
                if abbr[i] == '0':
                    return False
                
                # Get the count & append
                j = i+1
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                # print(abbr[i:j])
                count = int(abbr[i:j])
                
                if count > len(word) - j+1:
                    return False

                parsedAbbr.extend([''] * count)

                # Update i so that it starts from next char
                i = j
                # index += count
            
            # Characters
            else:
                parsedAbbr.append(abbr[i])
                i += 1
        # print([char for char in word])
        # print(parsedAbbr)
        if len(parsedAbbr) != len(word):
            return False
        for i in range(len(word)):
            if parsedAbbr[i] != '' and parsedAbbr[i] != word[i]:
                return False
        return True

            
            
