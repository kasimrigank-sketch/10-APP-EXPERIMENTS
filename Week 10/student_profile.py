def student_profile(name):
  """
  Creates a profile for a student and returns a function to add marks.
  
  Args:
    name: The name of the student.
    
  Returns:
    A nested function 'add_marks' that can be used to update the student's record.
  """
  marks_list = [] # This list is enclosed by the add_marks function

  def add_marks(subject, mark):
    """
    Nested function to add a mark and calculate the average.
    It has access to 'name' and 'marks_list' from the outer scope.
    """
    marks_list.append(mark)
    average = sum(marks_list) / len(marks_list)
    print(f"--- {name}'s Profile ---")
    print(f"Added mark for {subject}: {mark}")
    print(f"Current Marks: {marks_list}")
    print(f"Updated Average: {average:.2f}")
    print("-" * 25)
    
  return add_marks

# --- Demonstration ---
# Create a profile for a student named Alex
alex_profile = student_profile("Alex")

# Now use the returned function to add marks for Alex
alex_profile("Math", 85)
alex_profile("Science", 92)
alex_profile("History", 78)