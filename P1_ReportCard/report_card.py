# Student Report Card Generator

student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")

print("\nEnter Marks:")

math = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))

marks = {
    "Math": math,
    "Science": science,
    "English": english
}

total = sum(marks.values())
average = total / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n===== REPORT CARD =====")
print(f"Student ID   : {student_id}")
print(f"Student Name : {student_name}")

print("\nMarks:")
for subject, mark in marks.items():
    print(f"{subject}: {mark}")

print("\nTotal   :", total)
print("Average :", round(average, 2))
print("Grade   :", grade)
print("========================")