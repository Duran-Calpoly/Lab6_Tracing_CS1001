"""CS 1001 Lab Tracing 6 - Day 1
Mutation and aliasing.
"""

# Task 1 - Mutation and Aliasing
first = [2, 4, 6]
second = first
second.append(8)

print(first)
print(second)


# Task 2 - Aliasing vs. Separate Lists
a = [1, 2, 3]
b = a
c = [1, 2, 3]

b.append(4)

print(a)
print(b)
print(c)
