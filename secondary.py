# -------------------- Section 2 -------------------- #

# ---------- Part 1 | Patterns ---------- #
print(
    '>> Section 2\n'
    '>> Part 1\n'
)

# 1 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   b. Prompt input from the user in the form of an integer. Save to a variable named size.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#   >> size... 4
#
#   $$$$ size = 4, i = 0, s = size-i = 4 symbols
#    $$$ size = 4, i = 1, s = size-i = 3 symbols
#     $$ size = 4, i = 2, s = size-i = 2 symbols
#      $ size = 4, i = 3, s = size-i = 1 symbol
#
# Write Code Below #
s = input('>> symbol... ')
size = int(input('>> size... '))

for i in range(size):
    print(' ' * i + s * (size - i))
print()
# 2 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using two for loops, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#
#
# Write Code Below #
s = input('>> symbol | ')
n = int(input('Enter a number: '))

start = -n
stop = n 
step = 1

for i in range(start,stop, step):
    print(s * (abs(i) + 1))
print()

# 3 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using two for loops, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#
#
# Write Code Below #
s = input('>> symbol... ')

for i in range(1,5):
    print(s * i)

for i in range(5,0,-1): 
    print(s * i)

print() 
# ---------- Part 2 | Mathematical Patterns ---------- #
print(
    '>> Section 2\n'
    '>> Part 2\n'
)

# 1 - for Loop | Sum n
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate the sum of all numbers between 0 and n, and print the value.
#
#   sum = n + n - 1 + n - 2 + n - 3
#   
#   n --> represents position
#
#   EXAMPLE: 5 --> 5 + 4 + 3 + 2 + 1
#                  1 + 2 + 3 + 4 + 5
#
# Example Output
#
#   >> n = 10
#   >> 55
#
# Write Code Below #
n = int(input('Enter a whole number: '))
result = 0 

for i in range(1, n + 1):
    result = result + i
    print(result, 'result')
print()
# range(stop)
# range(start, stop)

# 1 - for Loop | n!
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate n! using loops.
#
#   n! or n factorial is equal to n * (n - 1) * (n - 2) * ... * 1
#
#   EXAMPLE: 5 --> 5 * 4 * 3 * 2 * 1
#
#
# Example Output
#
#   >> n = 10
#   >> 55
#
# Write Code Below #
n = int(input('>> integer | '))
result = 1

for i in range(1, n + 1):
    result = result * i
    print(result, 'result')