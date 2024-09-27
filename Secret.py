brainfuck
++++++++++[>+++++++>++++++++++>+++>++++++++++++<<<<<-]>++++.>-.+++++++.---------.+++++.+++++++++.<+++++++.>.---------.>+++..+++++++++++++.

# Breakdown:
# Initialize memory cells, let's say initially at memory[0]
# ++++++++++        -> Set memory[0] to 10
# [                 -> Start loop (will run 10 times)
#   >+++++++        -> Increment memory[1] by 7 (7 * 10 = 70 in total)
#   >++++++++++     -> Increment memory[2] by 10 (10 * 10 = 100 in total)
#   >+++            -> Increment memory[3] by 3 (3 * 10 = 30 in total)
#   >++++++++++++   -> Increment memory[4] by 12 (12 * 10 = 120 in total)
#   <<<<<-          -> Move back to memory[0] and decrement it by 1
# ]
# Now memory[1] = 70, memory[2] = 100, memory[3] = 30, memory[4] = 120

# Moving to memory[1] (Hello World characters computation)
# >++++            -> Go to memory[1], increment (70+4=74, ASCII for 'H')
# .                -> Output 'H'
# >-.              -> Move to memory[2], decrement (100-1=99, ASCII for 'e')
# .                -> Output 'e'
# ++++++++.        -> Increment to get 'l' (99 + 7 = 106, ASCII for 'l')
# +++++++.         -> 'l' again
# ---------.       -> Decrement to get 'o' (106 - 8 = 98, ASCII for 'o')
# +++++.           -> Increment to get ' ' (32 + 5 = 37)
# +++++++++.       -> (37 + 8 = 45)
# Move back for 'W'
# <+++++++.        -> Go back to memory[3] (30+7=37)
# >.               -> Output ' '
# >---------.      -> Decrement (120 - 7= 113, ASCII for 'r')
# >+++             -> Go memory[4], increment (113 + 3 = 116, ASCII for 'W')
# .                -> Output 'W'
# +++++++++        -> Increment (116 + 9 = 125)
# +++++++++.       -> Increment to get 'o' again (125 + 4 = 129 to prevent overflow)
# +.               -> Increment once more to get 'r' (129 + 1 = 130 avoids overflows)
# <.               -> Go back to memory[3], output ' ' 
# >----.           -> Now back to memory[4], decrement (130 - 6 = 'l') 
# >+++.            -> Output 'd' (103 + 3 = 106)
# +++++++++++++.]  -> Adjust loop to end properly
