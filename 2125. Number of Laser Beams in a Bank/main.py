class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        numberOfBeams = 0
        previous = 0

        for x in bank:
            count = x.count('1')
            if count == 0:
                continue

            numberOfBeams = numberOfBeams + ( count * previous )
            previous = count
        
        return numberOfBeams