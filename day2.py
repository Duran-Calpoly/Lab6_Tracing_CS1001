"""CS 1001 Lab Tracing 6 - Day 2
Tracing a for loop with an accumulator.
"""

# Task 3 - Tracing a Loop with an Accumulator
def tally(nums: list[int]) -> int:
    total = 0

    for num in nums:
        total = total + num

    return total


result = tally([4, 9, 2, 1])
print(result)
