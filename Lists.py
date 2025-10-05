# ======================================
# ❓ Question 1: Remove Duplicates from a List
# ======================================

# 📝 My Approach
def remove_duplicates_basic(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


# ✅ Optimal Approach
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# 🔎 Testing
print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))  # [1, 2, 3, 4, 5]


# ======================================
# ❓ Question 2: Find the Second Largest Element in a List
# ======================================

# 📝 My Approach
def second_largest_basic(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]


# ✅ Optimal Approach
def second_largest(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    return second


# 🔎 Testing
print(second_largest([10, 5, 8, 20, 15]))  # 15


# ======================================
# ❓ Question 3: Rotate a List Right by k Positions
# ======================================

# 📝 My Approach
def rotate_right_basic(lst, k):
    for _ in range(k):
        lst.insert(0, lst.pop())
    return lst


# ✅ Optimal Approach
def rotate_right(lst, k):
    n = len(lst)
    k %= n
    return lst[-k:] + lst[:-k]


# 🔎 Testing
print(rotate_right([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]


# ======================================
# ❓ Question 4: Pair Sum Problem (Find all pairs that sum to target)
# ======================================

# 📝 My Approach
def pair_sum_basic(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs


# ✅ Optimal Approach
def pair_sum(lst, target):
    seen = set()
    pairs = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)


# 🔎 Testing
print(pair_sum([1, 2, 3, 4, 5, 6], 7))  # [(1,6), (2,5), (3,4)]


# ======================================
# ❓ Question 5: Flatten a Nested List
# ======================================

# 📝 My Approach
def flatten_basic(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            for j in i:
                if isinstance(j, list):
                    for k in j:
                        result.append(k)
                else:
                    result.append(j)
        else:
            result.append(i)
    return result


# ✅ Optimal Approach
def flatten(lst):
    result = []
    stack = lst[::-1]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            result.append(item)
    return result


# 🔎 Testing
print(flatten([1, [2, [3, 4], 5], [6, 7]]))  # [1, 2, 3, 4, 5, 6, 7]
