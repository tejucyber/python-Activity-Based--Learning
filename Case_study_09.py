hotel = int(input("Hotel cost in foreign currency: "))
food = int(input("Food cost in foreign currency: "))
rate = float(input("Exchange rate: "))

total = (hotel + food) * rate
total = total + total * 2 / 100

print("Total Cost in Rupees =", total)

if total <= 20000:
    print("Within Budget")
else:
    print("Budget Exceeded")