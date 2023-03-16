l = input().split()
interval_num = int(l[0])
time = int(l[1])

total_intervals = []

for i in range(interval_num):
    interval = int(input())
    counter = interval
    while counter <= time:
        total_intervals.append(counter)
        counter += interval

finish = [*set(total_intervals)]
print(finish)
print(len(finish))
