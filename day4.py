"""CS 1001 Lab Tracing 6 - Day 4
Higher-level sequence patterns and integrated tracing.
"""

# Task 6 - Evaluating List Comprehensions
# Part A - Basic List Comprehension
more = [x + 1 for x in [1, 2, 3, 4]]
print(more)


# Part B - Calling a Function During a Comprehension
def square(n: int) -> int:
    return n * n


squares = [square(x) for x in [1, 2, 3, 4]]
print(squares)


# Part C - Filtering Values
def check(n: int) -> bool:
    return n > 2


filtered = [x for x in range(5) if check(x)]
print(filtered)


# Part D - Filtering and Transforming
def inc(m: int) -> int:
    return m + 1


answer = [inc(x) for x in range(5) if check(x)]
print(answer)


# Task 7 - Putting It All Together
def process(values: list[int], output: list[int]) -> int:
    total = 0

    for value in values:
        if value > 0:
            total = total + value
            output.append(value * 2)

    return total


source = [-1, 3, 0, 5]
result = []
alias = result
total = process(source, alias)

print(source)
print(result)
print(alias)
print(total)
