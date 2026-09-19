import csv

filename = "students.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])

    writer.writerow(["Harini", 20, "CSE"])
    writer.writerow(["Anu", 21, "ECE"])
    writer.writerow(["Ravi", 20, "EEE"])

print("Student Details:")

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(
            "Name:", row["Name"],
            ", Age:", row["Age"],
            ", Course:", row["Course"]
        )
