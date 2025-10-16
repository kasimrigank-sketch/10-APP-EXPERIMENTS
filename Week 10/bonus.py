def performance_bonus(salary):
  """Applies a 15% performance bonus."""
  return salary * 1.15

def festival_bonus(salary):
  """Applies a flat festival bonus of 5000."""
  return salary + 5000

def apply_bonus(func, salary):
  """
  A higher-order function that takes a bonus function and applies it to a salary.
  
  Args:
    func: The function to be applied (e.g., performance_bonus).
    salary: The initial salary.
    
  Returns:
    The updated salary after applying the bonus function.
  """
  updated_salary = func(salary)
  return updated_salary

# --- Demonstration ---
initial_salary = 50000

# Applying a performance bonus
salary_with_performance_bonus = apply_bonus(performance_bonus, initial_salary)
print(f"Initial Salary: ${initial_salary:,.2f}")
print(f"Salary after Performance Bonus (15%): ${salary_with_performance_bonus:,.2f}")

# Applying a festival bonus
salary_with_festival_bonus = apply_bonus(festival_bonus, initial_salary)
print(f"Salary after Festival Bonus ($5000): ${salary_with_festival_bonus:,.2f}")