i = input().split()
num_potions = int(i[0])
duration = int(i[1])
potions = []
for i in range(num_potions):
    potions.append(int(input()))

potions.sort()
potions.reverse()

maximum = potions[0]
time = duration * len(potions[1:])

if time < maximum:
    print("YES")
else:
    print("NO")