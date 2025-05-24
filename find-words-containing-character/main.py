class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        index = 0
        for word in words:
            if x in word:
                output.append(index)
            index+=1
        return output

                