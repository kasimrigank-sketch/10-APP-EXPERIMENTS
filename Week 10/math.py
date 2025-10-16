# --- Define some math operations ---
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    return "Error: Division by zero"
  return a / b

def operate(func, a, b):
  """
  A higher-order function that applies a given math function to two numbers.
  
  Args:
    func: The math function to apply (e.g., add, subtract).
    a: The first number.
    b: The second number.
    
  Returns:
    The result of the operation.
  """
  return func(a, b)

# --- Demonstration ---
print(f"Addition (10, 5): {operate(add, 10, 5)}")
print(f"Subtraction (10, 5): {operate(subtract, 10, 5)}")
print(f"Multiplication (10, 5): {operate(multiply, 10, 5)}")

# --- Adding a new operation without changing 'operate' ---
def power(a, b):
  """Calculates a to the power of b."""
  return a ** b

print(f"\nNew Power Operation (10, 5): {operate(power, 10, 5)}")