num_tolls = int(input())
least_amount = 0
amount = 0


for i in range(num_tolls):
    toll = input()
    take = True if toll[0] == 'T' else False
    cost = int(toll[2:])

    if take:
        amount -= cost
        
    else:
        least_amount = abs(amount)
        amount = cost
    print("Amount: ", amount)
    print("Least amount: ", least_amount)

if abs(amount) > least_amount:
    least_amount = abs(amount) 
    
print(least_amount)