"""CS 1001 Lab Tracing 6 - Day 3
Common loop patterns with lists and strings.
"""

# Task 4 - Building a List During Iteration
# Part A - Copying a List
def copy(nums: list[int]) -> list[int]:
    new_list = []

    for idx in range(len(nums)):
        new_list.append(nums[idx])

    return new_list


copied = copy([4, 9, 2, 1])
print(copied)


# Part B - Transforming Values
def increment_all(nums: list[int]) -> list[int]:
    new_list = []

    for value in nums:
        new_list.append(value + 1)

    return new_list


incremented = increment_all([4, 9, 2, 1])
print(incremented)


# Task 5 - Iterating over a String
def count_a(text: str) -> int:
    count = 0

    for char in text:
        if char == "a":
            count = count + 1

    return count


result = count_a("banana")
print(result)
