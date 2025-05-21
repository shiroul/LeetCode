class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index = len(a)-1

        if len(b) > index:
            index = len(b)-1
            a = '0' * (index - len(a)+1) + a
        else:   
            b = '0' * (index - len(b)+1) + b

        carry = 0
        output = ''
        while index >= 0:
            temp = 1 if a[index] == '1' else 0
            temp += 1 if b[index] == '1' else 0
            temp+=carry
            index-=1

            if temp == 2:
                carry = 1
                temp = 0
            elif temp == 3:
                carry = 1
                temp = 1
            else:
                carry = 0
            
            output = f'{temp}' + output
        
        return f'{carry}' + output if carry == 1 else output
