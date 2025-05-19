Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Grade to point mapping
... grade_points = {
...     "A": 5.0,
...     "B": 4.0,
...     "C": 3.0,
...     "D": 2.0,
...     "E": 1.0,
...     "F": 0.0
... }
... 
... # Initialize totals
... total_points = 0
... total_units = 0
... 
... print("Enter details for 6 courses:\n")
... 
... # Loop through 6 courses
... for i in range(1, 7):
...     print(f"Course {i}:")
...     course_name = input("  Course name: ")
...     unit = int(input("  Credit unit: "))
...     grade = input("  Grade (A-F): ").upper()
... 
...     if grade not in grade_points:
...         print("  Invalid grade entered. Please enter a grade from A to F.")
...         continue
... 
...     point = grade_points[grade]
...     total_points += point * unit
...     total_units += unit
... 
... # Calculate GPA
... if total_units == 0:
...     print("No valid course units entered.")
... else:
...     gpa = total_points / total_units
...     print(f"\nYour GPA for 6 courses is: {gpa:.2f}")
