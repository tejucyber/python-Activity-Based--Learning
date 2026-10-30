distance = int(input("Enter distance in km: "))
age = int(input("Enter age: "))

fare = distance * 2

if age >= 60 or age <= 12:
    fare = fare / 2

fare = fare + 30
print("Railway Fare =", fare)