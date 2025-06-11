# https://neetcode.io/problems/string-encode-and-decode
# Time: O(n)
# Space: O(n)

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        for word in strs:
            encoded.append(f"{len(word)}#{word}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        output = []
        while i < len(s):
            start = i
            while s[i] != "#":
                i += 1
            # end is exclusive
            wordLen = int(s[start:i])

            word = s[i+1: i+1+wordLen]
            output.append(word)
            i += 1 + wordLen
        return output


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))