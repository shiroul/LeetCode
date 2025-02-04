nums = [3,2,4]
target = 6

temp = {}
output = 0

for i, num in enumerate(nums):
    output = target - num

    if output in temp:
        print('banananna')
        break

    print(output, temp, output in temp)

    temp[num] = i
    
    