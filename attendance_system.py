students = ["Rahul", "Arjun", "Sai", "Ravi"]

print("Student Attendance System")
print("-------------------------")

for student in students:
    status = input(f"Is {student} present? (yes/no): ")
    print(f"{student} - {status}")
