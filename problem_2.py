'''
You are given a puzzle like this:
7 __ 10 __ 2

Each __ may be filled with a "+" (plus) or "-" (minus), producing a value k. For all
combinations of plus and minus, find the value of k that is closest to 0.
In the above case, there are 4 combinations, each producing a different value:
7 + 10 + 2 = 19
7 + 10 - 2 = 15
7 - 10 + 2 = -1
7 - 10 - 2 = -5
Of all these combinations, the value that is closest to zero is -1. So the answer is -1. If
there is more than one number that is closest, print the absolute value.

Input Format:
You are given a comma separated string of numbers. Each number is ≥ 0 and <10^5
.

There could be up to 100 numbers in a string.
Sample Input/Output:
Enter digits: 7,10,2
Value close to zero is -1
Enter digits: 1,2,3,4
Value close to zero is 0
'''

# use recursion
possible_sum = set()
def solve_puzzle_rec(digits, index, total):
    if index == len(digits):
        possible_sum.add(total)
        return abs(total)
    return min(solve_puzzle_rec(digits, index + 1, total + digits[index]),
               solve_puzzle_rec(digits, index + 1, total - digits[index]))

def solve_puzzle(digits):
    digits = [int(d) for d in digits.split(',')]
    abs_total = solve_puzzle_rec(digits, 1, digits[0])
    if -abs_total in possible_sum:
        if abs_total not in possible_sum:
            return -abs_total
        return abs_total
    return abs_total 

print(solve_puzzle('7,10,2'))