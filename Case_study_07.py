price = int(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 2000:
    total = total - total * 10 / 100
elif total >= 1000:
    total = total - total * 5 / 100

print("Final Bill =", total)