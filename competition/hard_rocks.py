import math

hours = int(input()) / 3600

answer = (math.ceil(hours) - hours) * 60
print(math.ceil(answer))