class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        output = []
        for string in queries:
            s, p = 0, 0
            cantMatch = False
            while s < len(string) and p < len(pattern):
                schar, pchar = string[s], pattern[p]
                if schar == pchar:
                    p += 1
                elif schar.isupper():
                    output.append(False)
                    cantMatch = True
                    break
                s += 1
            if cantMatch:
                continue
            while s < len(string):
                schar = string[s]
                if schar.isupper():
                    output.append(False)
                    cantMatch = True
                    break
                s += 1
            if cantMatch:
                continue
            if p >= len(pattern):
                output.append(True)
            else:
                output.append(False)
        return output

