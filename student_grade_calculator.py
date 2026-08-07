# ============================================
#       STUDENT GRADE CALCULATOR
#       BCA Mini Project
# ============================================

print("=" * 50)
print("          STUDENT GRADE CALCULATOR")
print("=" * 50)

name = input("Enter Student Name: ")
register_no = input("Enter Register Number: ")

print("\nEnter marks out of 100 for each subject")

python = float(input("Python: "))
dbms = float(input("DBMS: "))
java = float(input("Java: "))
computer_network = float(input("Computer Network: "))
data_structure = float(input("Data Structure: "))

total = python + dbms + java + computer_network + data_structure
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if (python >= 35 and dbms >= 35 and java >= 35
        and computer_network >= 35 and data_structure >= 35):
    result = "PASS"
else:
    result = "FAIL"

print("\n" + "=" * 50)
print("              STUDENT RESULT")
print("=" * 50)

print("Student Name   :", name)
print("Register No.   :", register_no)
print("-" * 50)

print("Python         :", python)
print("DBMS           :", dbms)
print("Java           :", java)
print("Computer Net.  :", computer_network)
print("Data Structure :", data_structure)

print("-" * 50)
print("Total Marks    :", total, "/ 500")
print("Percentage     :", round(percentage, 2), "%")
print("Grade          :", grade)
print("Result         :", result)

print("=" * 50)
print("        Thank You!")
print("=" * 50)