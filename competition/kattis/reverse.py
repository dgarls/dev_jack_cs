numNums = int(input())
lst = []
for i in range(numNums):
    lst.append(input())

for idx, num in enumerate(lst):
    print(lst[len(lst) - idx - 1])
