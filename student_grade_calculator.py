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

print("\n" + "=" * 50)
print("                  RESULT")
print("=" * 50)

print("Student Name    :", name)
print("Register Number :", register_no)
print("Total Marks     :", total, "/ 500")
print("Percentage      :", percentage, "%")
print("Grade           :", grade)

print("=" * 50)