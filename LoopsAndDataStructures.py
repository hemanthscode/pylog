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


# ======================================
# ❓ Question 2: Count Vowels in a String
# ======================================

# 📝 My Approach
def countVowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    print(count)


# ✅ Optimal Approach
def count_vowels(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)


# 🔎 Testing
countVowels("Python Programming")           # 4
print(count_vowels("Python Programming"))   # 4


# ======================================
# ❓ Question 3: Students with Scores Above 75
# ======================================

# 📝 My Approach
def highScorers(students):
    for name, score in students.items():
        if score > 75:
            print(name)


# ✅ Optimal Approach
def high_scorers(students, cutoff=75):
    if not isinstance(students, dict):
        raise TypeError("Input must be a dictionary")
    
    return [name for name, score in students.items() if score > cutoff]


# 🔎 Testing
students = {"Alice": 90, "Bob": 60, "Charlie": 80}
highScorers(students)                        # Alice, Charlie
print(high_scorers(students))                # ['Alice', 'Charlie']


# ======================================
# ❓ Question 4: Common Elements in Two Sets
# ======================================

# 📝 My Approach
def commonElements(set1, set2):
    print(set1 & set2)


# ✅ Optimal Approach
def common_elements(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError("Both inputs must be sets")
    
    return set1.intersection(set2)


# 🔎 Testing
commonElements({1, 2, 3, 4}, {3, 4, 5, 6})   # {3, 4}
print(common_elements({1, 2, 3, 4}, {3, 4, 5, 6}))  # {3, 4}


# ======================================
# ❓ Question 5: Print Pattern with Nested Loops
# ======================================

# 📝 My Approach
def pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()


# ✅ Optimal Approach
def star_pattern(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    return "\n".join(" ".join("*" for _ in range(i)) for i in range(1, n + 1))


# 🔎 Testing
pattern(5)
print(star_pattern(5))
