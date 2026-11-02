Aim: Check scholarship eligibility using marks, attendance, and family income.
Algorithm
1. Start
2. Input name, marks, attendance, income
3. Check eligibility conditions
4. IF all conditions are true
5. Display eligible / not eligible
6. Stop
Flowchart
Start
Input name, marks, attendance, income
Check eligibility conditions
IF all conditions are true
Display eligible / not eligible
Stop
Pseudocode
START
INPUT name, marks, attendance, income
IF marks >= 80 AND attendance >= 75 AND income <= 50000
PRINT "Eligible for scholarship"
ELSE
PRINT "Not eligible"
STOP
Python Program
name = input("Enter name: ")
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
income = int(input("Enter family income: "))
if marks >= 80 and attendance >= 75 and income <= 50000:
print(name, "Eligible for scholarship")
else: