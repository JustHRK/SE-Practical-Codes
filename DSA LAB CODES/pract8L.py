# Read the marks obtained by students of second year in an online examination of particular subject. Find out maximum and minimum marks obtained in that subject. Use heap data structure. Analyze the algorithm.

import heapq

def find_max_min_marks(marks):
    if not marks:
        return None, None

    max_marks = max(marks)
    min_marks = min(marks)

    return max_marks, min_marks

# Read marks from user input
def read_marks():
    marks = []
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        mark = int(input(f"Enter the marks for student {i+1}: "))
        marks.append(mark)

    return marks

# Example usage:
marks_obtained = read_marks()
print("Marks obtained:", marks_obtained)

max_marks, min_marks = find_max_min_marks(marks_obtained)
print("Maximum marks:", max_marks)
print("Minimum marks:", min_marks)
