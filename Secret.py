brainfuck
>++++++++[<+++++++++>-]<. >++++[<+++++++>-]<+.+++++++..+++. 
>>>++++++++[<+++++++>-]<.>>>++++++++++[<+++++++++++>-]<-. 
<<<<.+++.------.--------. >>>+. 

# Brainfuck Explanation:
# Initialize memory block and set pointer to 0
>++++++++         # Initialize cell0 with value 8
[                   # Loop until cell0 is zero
  <+++++++++       # Add 9 to cell to the left (cell1); this loop executes 8 times
  >                # Move back to cell0
  -                # Decrement cell0
]                   # End of the loop. Now cell1 = 72 ('H')
<.                  # Move back to cell1 and output its value ('H')
# Outputting 'e'
>++++            # Move to cell0 and add 4
[                # Loop until cell0 is zero
  <+++++++       # Add 7 to cell to the left (cell1); this loop executes 4 times
  >              # Move back to cell0
  -              # Decrement cell0
]                # End of the loop. Now cell1 = 101 ('e')
<.               # Move back to cell1 and output its value ('e')
# Outputting 'l'
+++++++         # Add 7 to cell0 (8+7 = 15)
.               # Output cell0's value ('o')
.               # Output cell0's value again ('o')
+++             # Add 3 to cell0 (15+3 = 18)
.               # Output cell0's value ('r')
# Outputting 'o'
>>>++++++++         # Move to cell0 and add 8
[                   # Loop until cell0 is zero
  <+++++++          # Add 7 to cell to the left (cell1); this loop executes 8 times
  >                 # Move back to cell0
  -                 # Decrement cell0
]                   # End of the loop. Now cell1 = 111 ('o')
<.                  # Move back to cell1 and output its value ('o')
# Outputting 'W'
>>>++++++++++         # Move to cell0 and add 10
[                     # Loop until cell0 is zero
  <+++++++++++        # Add 11 to cell to the left (cell1); this loop executes 10 times
  >                   # Move back to cell0
  -                   # Decrement cell0
]                     # End of the loop. Now cell1 = 87 ('W')
<-.                   # Move back to cell1 and output its value ('W')
# Outputting 'o'
<<<<<.                 # Move to the cell -5 (which was the cell containing 'o')
+++                   # Add 3 to cell to the left
.                     # Output cell's value 'o'
# Outputting 'r'
------                # Move to the cell, it was already holding 111
.                     # Output cell's value 'r'
# Outputting 'l'
--------             # Move to the left cell holding 104 (move value from 'H')
.                    # Output cell's value 'H'
# Outputting 'd'
>>>.                  # Output cell's value 'd'
