# Time:
# - addWord(): O(n)
# - search(): in the worst case, it will be O(26^n) where n is the number of '.' in the word
# since the number of wildcards is capped at 2, the worst case will be O(max(n, 26^2))
# Space: O(n * 26^n)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(pos, node):
            # Reached the end of word
            if pos == len(word):
                return node.isEnd

            searchChar = word[pos]
            # If searchChar is wildcard char
            if searchChar == ".":
                for possibleChar in node.children:
                    # If any path returns True, word exists
                    if dfs(pos + 1, node.children[possibleChar]):
                        return True
                # None of the paths matched
                return False
            
            # If searchChar is alpha and exists
            elif searchChar in node.children:
                return dfs(pos + 1, node.children[searchChar])

            return False
        
        # Start the search
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)