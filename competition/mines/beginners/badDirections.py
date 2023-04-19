tests = int(input())

for test in range(tests):
    i = [int(x) for x in input().split()]
    key = i[0]
    num = i[1]
    numStr = str(num)
    decoded = ''

    for n in numStr:
        n = int(n)
        n += key
        n = n % 10
        decoded += str(n)
    
    print(decoded)
