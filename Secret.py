# This script is written in Brainfuck, an esoteric programming language.
# Brainfuck operates on an array of memory cells, each initially set to zero.
# The language uses a minimalistic set of commands.
# Commands are: > (increment memory pointer), < (decrement memory pointer),
# + (increment byte at memory pointer), - (decrement byte at memory pointer),
# . (output byte at memory pointer to stdout), , (input byte to memory pointer),
# [ (jump past matching ] if byte at memory pointer is zero),
# ] (jump back to matching [ if byte at memory pointer is non-zero).

# Initialize required memory cells for 'H', 'e', 'l', 'o', 'W', 'r', 'd' using the patterns below.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
<<<<<++++++.

# Memory cells now contain: 72 ('H'), 101 ('e'), 108 ('l'), 111 ('o'), 87 ('W'), 114 ('r'), 100 ('d').
# We will now print "Hello World" using these memory cells.

# Print 'H'
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.

# Move to 'e'
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
# Move to 'l'
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
# Reuse 'l'
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
# Move to 'o'
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
# Print space by moving to a new memory cell and setting it to 32
>++++++++++++++++++++++++++++++++++++++++++++++++.
# Move to 'W'
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
# Move back to 'o'
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
# Move to 'r'
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
# Move to 'l'
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
# Move to 'd'
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.

# The output should be "Hello World" now. End of program.