def filter_students(criteria, students):
  """
  Filters a list of students based on a given criteria function.
  
  Args:
    criteria: A function that returns True or False for a student.
    students: A list of student dictionaries.
    
  Returns:
    A new list containing only the students who meet the criteria.
  """
  return [student for student in students if criteria(student)]

# --- Demonstration ---
students = [
    {"name": "Alice", "cgpa": 8.5},
    {"name": "Bob", "cgpa": 7.9},
    {"name": "Charlie", "cgpa": 9.1},
    {"name": "David", "cgpa": 8.0},
    {"name": "Eve", "cgpa": 9.5}
]

# Using a lambda function to define the filtering criteria on the fly
high_achievers = filter_students(lambda s: s["cgpa"] > 8, students)

print("All students:")
print(students)
print("\nStudents with CGPA > 8:")
print(high_achievers)