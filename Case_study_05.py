budget = int(input("Enter budget: "))
data = int(input("Enter required data in GB: "))

if budget >= 199 and data <= 2:
    print("Choose Basic Plan")
elif budget >= 299 and data <= 5:
    print("Choose Smart Plan")
elif budget >= 399 and data <= 10:
    print("Choose Premium Plan")
else:
    print("No suitable plan")