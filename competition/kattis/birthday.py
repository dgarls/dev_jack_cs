names = []
scores = []
dates = []

numFriends = int(input())

for f in range(numFriends):
    friend = input().split()
    name = friend[0]
    score = int(friend[1])
    date = friend[2]
    names.append(name)
    scores.append(score)
    dates.append(date)
    
matchingDates = []
indexes = []

for idx, date in enumerate(dates):
    if idx in indexes:
        continue
    indexes.append(idx)
    temp = [date]
    for index, date2 in enumerate(dates[idx + 1:]):
        if date == date2:
            temp.append(date)
            indexes.append(index + idx + 1)
    matchingDates.append(temp)

print(matchingDates)

# I can't do this anymore