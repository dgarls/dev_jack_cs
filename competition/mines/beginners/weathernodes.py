from statistics import mean

num_temps = int(input())
temps = []
for i in range(num_temps):
    temps.append(float(input()))

avg = mean(temps)
bad_count = 0

for temp in temps:
    if abs(avg - temp) > 10: 
        bad_count += 1

print(bad_count)