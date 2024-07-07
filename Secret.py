brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++.>+++.------.--------.>+.>.

# Explanation:
# ++++++++++        -> This sets the first cell to 10
# [                 -> Start of loop, repeat until first cell is 0
#   >+++++++        -> Move to the second cell and increment it 7 times (second cell = 70)
#   >++++++++++     -> Move to the third cell and increment it 10 times (third cell = 100)
#   >+++            -> Move to the fourth cell and increment it 3 times (fourth cell = 30)
#   >+              -> Move to the fifth cell and increment it once (fifth cell = 10)
#   <<<<-           -> Move back to the first cell and decrement it once
# ]                 -> End of loop

# Now that cells are set up:
# [ 10, 70, 100, 30, 10 ]

# We will start printing "Hello, World!"

# Print 'H'
# >++.              -> Move to the second cell and print character (cell 70, ASCII 'H')

# Print 'e'
# >+.               -> Move to the third cell and print character (cell 100, ASCII 'e')

# Print 'l'
# ++++++++.         -> Increment the third cell 7 times (107, ASCII 'l'), print character

# Print 'l'
# .                 -> Print character at the third cell again

# Print 'o'
# +++.              -> Increment the third cell 3 times (110, ASCII 'o'), print character

# Print ','
# >++.              -> Move to the fourth cell and print character (cell 30, ASCII ',')

# Print ' '
# <<+++++++++++++.  -> Move back to the second cell, increment it 15 times (85, ASCII ' '), print character

# Print 'W'
# >+++.             -> Move to the third cell, increment its content 3 times (103, ASCII 'W'), print character

# Print 'o'
# ------.           -> Decrement the third cell 6 times (97, ASCII 'o'), print character

# Print 'r'
# --------.         -> Decrement the third cell 8 times (89, ASCII 'r'), print character

# Print 'l'
# >+.               -> Move to the fourth cell and print character (cell 30, ASCII 'l')

# Print 'd'
# >.                -> Move to the fifth cell and print character (cell 10, ASCII 'd')
