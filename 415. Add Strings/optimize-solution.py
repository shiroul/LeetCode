class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        output = []
        carry = 0

        length1, length2 = len(num1)-1, len(num2)-1

        while length1 >= 0 or length2 >= 0 or carry:
            number1 = ord(num1[length1]) - 48 if length1 >= 0 else 0
            number2 = ord(num2[length2]) - 48 if length2 >= 0 else 0

            carry += (number1+number2)
            output.append(chr(carry%10+48))
            carry = carry // 10

            length1 -=1
            length2 -=1
        
        return ''.join(output[::-1])