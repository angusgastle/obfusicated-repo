brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>++++.+++++++++++.<+++++.>-----.-------.

# Initialize the memory and set up the cell values:
# Memory: [10, 0, 0, 0, 0]
# The loop [>+++++++>++++++++++>+++>+<<<<-] will run 10 times and modify the memory as follows:
# Memory: [0, 70, 100, 30, 10]

# First, print 'H' (72):
# ++             increment Cell[1] by 2 to get 72
# .              output 'H'

# Print 'e' (101):
# >              move to Cell[2]
# +              increment Cell[2] by 1 to get 101
# .              output 'e'

# Print 'l' (108):
# +++++++        increment Cell[2] by 7 to get 108
# .              output 'l'
# .              output 'l'

# Print 'o' (111):
# +++            increment Cell[2] by 3 to get 111
# .              output 'o'

# Print ' ' (32):
# >              move to Cell[3]
# .              output ' ' (space character)

# Print 'W' (87):
# <<             move back to Cell[1]
# +++++++++++++++ increment Cell[1] by 15 to get 87
# .              output 'W'

# Print 'o' (111):
# >++++           move to Cell[2] and increase by 4 to get 111
# .              output 'o'

# Print 'r' (114):
# +++++++++++     increment Cell[2] by 11 to get 114
# .              output 'r'

# Print 'l' (108):
# <+++++          move to Cell[1] and increase by 5 to get 108
# .              output 'l'

# Print 'd' (100):
# >-----         move to Cell[2] and decrement by 5 to get 100
# .              output 'd'

# Terminate the program with extra steps (non-functional) for complexity:
# -------      decrement Cell[2] by 7 to nearly zero it out
