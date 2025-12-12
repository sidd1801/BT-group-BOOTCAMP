# solution.py

def student_report(name, s1, s2, s3):
    """
    Returns a dictionary containing:
    - total marks
    - average marks
    - class secured
    """

    total = s1 + s2 + s3
    average = total / 3

    # Determine class
    if average >= 60:
        grade = "1st Class"
    elif average >= 50:
        grade = "2nd Class"
    elif average >= 35:
        grade = "Pass Class"
    else:
        grade = "Fail"

    return {
        "name": name,
        "total": total,
        "average": average,
        "class": grade
    }


if __name__ == "__main__":
    name = input("Enter student's name: ")
    s1 = float(input("Enter marks in Subject 1: "))
    s2 = float(input("Enter marks in Subject 2: "))
    s3 = float(input("Enter marks in Subject 3: "))

    report = student_report(name, s1, s2, s3)

    print("\n--- STUDENT REPORT CARD ---")
    print("Name:", report["name"])
    print("Total Marks:", report["total"])
    print("Average:", report["average"])
    print("Class Secured:", report["class"])
