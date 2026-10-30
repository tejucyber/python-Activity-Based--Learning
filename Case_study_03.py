# hospital bill
consultation = int(input("Consultation charge: "))
test = int(input("Test charge: "))
treatment = int(input("Treatment charge: "))

total = consultation + test + treatment

age = int(input("Enter age: "))

if age >= 60:
    total = total - total * 10 / 100

print("Total Bill =", total)