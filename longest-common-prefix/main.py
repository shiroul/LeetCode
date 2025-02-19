class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        output = ''

        for x in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][x] != strs[-1][x]:
                break
            output+=strs[0][x]
        return output