class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for x in range(1, n+1):
            if x % 3 == 0 and x % 5 == 0:
                output.append('FizzBuzz')
            elif x % 3 == 0:
                output.append('Fizz')
            elif x % 5 == 0:
                output.append('Buzz')
            else:
                output.append(f'{x}')
        
        return output