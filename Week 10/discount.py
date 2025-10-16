def discount_calculator(rate):
  """
  A function factory that creates a discount-applying function.
  
  Args:
    rate: The discount rate (e.g., 0.1 for 10%).
    
  Returns:
    A new function that takes a price and returns the discounted price.
  """
  def apply_discount(price):
    """
    Applies the discount. It 'remembers' the rate from its parent.
    """
    return price * (1 - rate)
  
  return apply_discount

# --- Demonstration ---
# 1. Create a specific discount function for 10% off
ten_percent_discount = discount_calculator(0.10)

# 2. Create another one for 25% off
twenty_five_percent_discount = discount_calculator(0.25)

# 3. Use the created functions
price = 2000
discounted_price_10 = ten_percent_discount(price)
discounted_price_25 = twenty_five_percent_discount(price)

print(f"Original Price: ${price:,.2f}")
print(f"Price after 10% discount: ${discounted_price_10:,.2f}")
print(f"Price after 25% discount: ${discounted_price_25:,.2f}")