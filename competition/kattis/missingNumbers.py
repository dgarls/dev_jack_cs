numNums = int(input())
nums = []
for i in range(numNums): 
    nums.append(int(input()))
correct = range(1, nums[-1])
counter = 0
for num in correct:
    if num not in nums:
        print(num)
        counter += 1

if counter == 0:
    print('good job')