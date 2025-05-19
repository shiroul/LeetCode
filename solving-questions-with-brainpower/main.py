class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        stop = len(questions)
        memo = {}


        def takeOrSkip(i):
            if i >= stop:
                return 0
            if i in memo:
                return memo[i]
            
            take = questions[i][0] + takeOrSkip(i+questions[i][1]+1)
            skip = takeOrSkip(i+1)

            memo[i] = take if take > skip else skip

            return memo[i]
        
        return takeOrSkip(0)