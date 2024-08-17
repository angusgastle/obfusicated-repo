perl
# Let's use Brainfuck, an esoteric programming language that is intentionally difficult to program in.
# The following Brainfuck program will output "Hello World!" character by character.
# Brainfuck operates on an array of memory cells, each initially set to zero.
# It uses a data pointer, initially pointing at the first memory cell.
# Each Brainfuck command is a single character:
# > : Increment the data pointer (to point to the next cell to the right).
# < : Decrement the data pointer (to point to the next cell to the left).
# + : Increment (increase by one) the byte at the data pointer.
# - : Decrement (decrease by one) the byte at the data pointer.
# . : Output the byte at the data pointer.
# , : Accept one byte of input, storing its value in the byte at the data pointer.
# [ : If the byte at the data pointer is zero, then instead of moving the instruction pointer forward
#     to the next command, jump it forward to the command after the matching ] command.
# ] : If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward
#     to the next command, jump it back to the command after the matching [ command.

# The below code uses the Brainfuck language to print "Hello World!" including the newline character at the end.

++++++++++                 # Cell 0 = 10
[                          # Loop until cell 0 is zero
    >+++++++               # Move to cell 1; add 7 to cell 1; this will be 70
    >++++++++++            # Move to cell 2; add 10 to cell 2; this will be 100
    >+++                   # Move to cell 3; add 3 to cell 3; this will be 30
    >+++                   # Move to cell 4; add 3 to cell 4; this will be 30
    >++++++++++            # Move to cell 5; add 10 to cell 5; this will be our carriage return (ascii 10)
    >++++++++              # Move to cell 6; add 8 to cell 6; this will be 80
    >++++++++++            # Move to cell 7; add 10 to cell 7; this will be 100
    >++                    # Move to cell 8; add 2 to cell 8; this will be 20
<<<<<<<<<-                 # Move back to cell 0; decrement cell 0 by 1; repeat until cell 0 is 0
]                          # End of loop when cell 0 is 0

# Now cell 1-8 have the following values correspondingly: 70, 100, 30, 30, 10, 80, 100, 20

>++.                      # Move to cell 1; increment to 72; output 'H'
>+.                       # Move to cell 2; increment to 101; output 'e'
+++++++.                  # Increment to 108; output 'l'
.                         # Output 'l'
+++.                      # Increment to 111; output 'o'
>++.                      # Move to cell 3; increment to 33; output 'W'
<<+.                      # Move to cell 1; increment to 104; output 'o'
------.                   # Decrement to 100; output 'r'
--------.                 # Decrement to 92; output 'l'
+++.                      # Increment to 95; output 'd'
>+.                       # Move to cell 5; increment to 11; output '!'
>+.                       # Move to cell 6; increment to 81; output newline
