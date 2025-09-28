# ======================================
# ❓ Question 1: Squares of Even Numbers in a List
# ======================================

# 📝 My Approach
def squaresOfEven(lst):
    evens = []
    for x in lst:
        if x % 2 == 0:
            evens.append(x * x)
    print(evens)


# ✅ Optimal Approach
def squares_of_even(lst):
    if not all(isinstance(x, int) for x in lst):
        raise TypeError("All elements must be integers")
    
    return [x ** 2 for x in lst if x % 2 == 0]


# 🔎 Testing
squaresOfEven([2, 4, 5, 3, 6, 7])      # [4, 16, 36]
print(squares_of_even([2, 4, 5, 3, 6, 7]))  # [4, 16, 36]
