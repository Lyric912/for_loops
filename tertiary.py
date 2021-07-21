# -------------------- Section 3 -------------------- #

# ---------- Part 1 | Patterns ---------- #
print(
    '>> Section 3\n'
    '>> Part 1\n'
)

# 1 - for Loop | Patterns
#   Create a function that will calculate and print the first n numbers of the fibonacci sequence.
#       n is specified by the user.
#
#   NOTE: You can assume that the user will enter a number larger than 2
#
# Example Output
#
#   >> size... 6
#
#   1, 1, 2, 3, 5, 8
# 
# Keep track of the last two numbers, and adjust
#   once you get the next one.
# Write Code Below #
n = int(input('Enter a number to get that many numbers of the fibonacci sequence: '))
n_minus1 = 1
n_minus2 = 1

print(1)
print(1)

for i in range(n - 2):
    new_num = n_minus1 + n_minus2
    print(new_num)
    n_minus2 = n_minus1
    n_minus1 = new_num


# num1 = 1
# sequence = 
# num_before = []
# fib = num_before + 
