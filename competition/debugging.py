import math

fail = float(input())
succeed = 1 - fail
required = int(input())
max_attempts = int(input())

chance = math.pow(succeed, required)
print(chance)
