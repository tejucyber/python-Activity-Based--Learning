material = int(input("Enter material cost: "))
labour = int(input("Enter labour cost: "))
machine = int(input("Enter machine cost: "))
selling = int(input("Enter total selling amount: "))

cost = material + labour + machine
profit = selling - cost

print("Total Cost =", cost)
print("Profit =", profit)

if profit >= 2000:
    print("Target Achieved")
else:
    print("Target Not Achieved")