letters = {'A' : 0, 'B' : 1, 'C': 2}

nums = input().split()
nums = [int(x) for x in nums]
nums.sort()

order = [x for x in input()]

new = []

for char in order:
    new.append(nums[letters.get(char)])

print(*new, sep=' ')