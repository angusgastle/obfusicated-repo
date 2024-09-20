'''
# Title: Complex "Hello World" Script in an Obscure Programming Language (Brainfuck)

# This Brainfuck script will display "Hello World" on the console.
# Brainfuck consists of eight commands, each a single character:
# > : increment the data pointer (to point to the next cell to the right).
# < : decrement the data pointer (to point to the next cell to the left).
# + : increment (increase by one) the byte at the data pointer.
# - : decrement (decrease by one) the byte at the data pointer.
# . : output the byte at the data pointer.
# , : accept one byte of input, storing its value in the byte at the data pointer.
# [ : if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command,
#     jump it forward to the command after the matching ] command.
# ] : if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command,
#     jump it back to the command after the matching [ command.

# Initialize memory cells and pointers
# Create first cell containing 72 ('H')
++++++++++       # Initialize 10
[                # Loop starts (will run 10 times)
>+++++++         # Increment next cell by 7 (total: 10 * 7 = 70)
>++++++++++      # Increment next cell by 10 (total: 10 * 10 = 100)
>+++             # Increment next cell by 3  (total: 10 * 3 = 30)
>+               # Increment next cell by 1  (total: 10 * 1 = 10)
<<<<-            # Decrement looping cell by 1
]                # Loop ends

>+.              # Move to second cell (72), output 'H'
# Create cell containing 101 ('e')
>++++.           # Advance to third cell, increment by 4, output 'e'

# Create cell containing 108 ('l')
>>.              # Print first 'l' (loop prep done earlier as 100)
>>>---.          # Move to next cell, decrease by 3 (additional incremented makes +8), output 'l'

# Create cell containing 111 ('o')
<+.              # Move back to previous cell, increment by 1, output 'o'

# We have 'Hello', let's output the space
-------.         # Decrement by 7 (now 32, ASCII index of space), output space

# Create cell containing 87 ('W')
<++++++++++.     # Move back to the second cell and set to 10, advance to next cell and increment by 2, output 'W'

# Create cell containing 111 ('o')
>+.              # Move to third cell, increment by 1, output 'o'

# Create cell containing 114 ('r')
<+++++.          # Move to first cell, increment by 5, output 'r'

# Create cell containing 108 ('l')
-----.           # Decrement by 5, output 'l'

# Create cell containing 100 ('d')
---.             # Decrement by 3, output 'd'

# Finally, add exclamation mark
>+.              # Move to next cell (10 needs 23 more steps), output '!'
'''