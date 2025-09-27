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

def sum_of_digits_optimal(num):
    num = abs(num)
    total = 0
    while num > 0:
        total+=num%10
        num//=10
    return total
print(sum_of_digits_optimal(996))



# ======================================
# ❓ Question 4: Print numbers with While Loop + Sum of Digits
# ======================================

# 📝 My Approach
num = 1
while num <= 20:
    print(num)
    num += 1


# ✅ Optimal Approach
def sum_of_digits(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# 🔎 Testing
print(sum_of_digits(123))   # 6
print(sum_of_digits(9876))  # 30


# ======================================
# ❓ Question 5: Break Statement Examples
# ======================================

# 📝 My Approach
for i in range(1, 101):
    if i == 50:
        break
    print(i)


# ✅ Optimal Approach (Login Simulation)
def login_system(correct_password="python123"):
    attempts = 0
    while True:
        pwd = input("Enter password: ")
        attempts += 1
        if pwd == correct_password:
            print("Access Granted ✅")
            break
        else:
            print("Wrong password ❌")
    return attempts


# 🔎 Testing (manual input required in console)
# login_system()


# ======================================
# ❓ Question 6: Continue Statement Examples
# ======================================

# 📝 My Approach
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


# ✅ Optimal Approach (Filter names not starting with 'A')
def filter_names(names):
    return [name for name in names if not name.startswith("A")]


# 🔎 Testing
names_list = ["Alice", "Bob", "Andrew", "Catherine", "Alex", "David"]
print(filter_names(names_list))  
# Output: ['Bob', 'Catherine', 'David']


# ======================================
# ❓ Question 7: Pass Statement Example
# ======================================

# 📝 My Approach
def check_number(num):
    if num < 0:
        pass
    else:
        print(num)


# ✅ Optimal Approach
def check_number_strict(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a number")
    
    if num < 0:
        pass  # reserved for future logic
    else:
        print(f"Valid number: {num}")


# 🔎 Testing
check_number_strict(5)   # Valid number: 5
check_number_strict(-2)  # No output


# ======================================
# ❓ Question 8: Combined Challenge
# ======================================

# 📝 My Approach
for i in range(1, 101):
    if i % 3 == 0:
        continue
    if i > 77:
        break
    print(i)


# ✅ Optimal Approach
def custom_loop(limit=100):
    for i in range(1, limit + 1):
        if i % 3 == 0:
            continue
        if i > 77:
            break
        print(i)


# 🔎 Testing
custom_loop()
