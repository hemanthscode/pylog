# ======================================
# ❓ Question 1: Check if a number is Even or Odd
# ======================================

# 📝 My Approach
def is_Even_Or_Odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


# ✅ Optimal Approach
def is_even_or_odd(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print("Even" if num % 2 == 0 else "Odd")


# 🔎 Testing
is_even_or_odd(15)  # FizzBuzz
is_even_or_odd(6)   # Even
is_even_or_odd(9)   # Odd


# ======================================
# ❓ Question 2: Check if a number is Positive, Negative, or Zero
# ======================================

# 📝 My Approach
num = -3

if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
elif num < 0:
    print("Negative")


# ✅ Optimal Approach
def check_number_sign(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a number (integer or float)")
    
    if num == 0:
        print("Zero")
    elif num > 0:
        print("Positive")
    else:
        print("Negative")


# 🔎 Testing
check_number_sign(0)   # Zero
check_number_sign(-5)  # Negative
check_number_sign(7)   # Positive


# ======================================
# ❓ Question 3: Print Natural Numbers and Multiplication Table
# ======================================

# 📝 My Approach
for x in range(1, 11):
    print(x)

for i in range(1, 11):
    print(f"7 x {i} = {i*7}")


# ✅ Optimal Approach
def get_multiplication_table(number, limit):
    if not isinstance(number, int):
        raise ValueError("Number must be an integer")
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be a positive integer")
    
    return [f"{number} x {i} = {number * i}" for i in range(1, limit + 1)]


# 🔎 Testing
table = get_multiplication_table(7, 10)
for line in table:
    print(line)
