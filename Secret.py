# Brainfuck script to display "Hello World"
# Brainfuck is an esoteric programming language created in 1993

# Start by setting up memory cells to hold the ASCII values of the characters
# Memory cells [0] to [12] will hold the values for "Hello World!"

++++++++++              # Cell 0 set to 10
[
    >+++++++>++++++++++ # Cell 1 set to 70, Cell 2 set to 100
    >+++>+<<<<-         # Move cells and decrement loop counter (cell 0)
]

# Set up the respective values
>++.                    # Cell 1 is 72 -> 'H'
>+.                     # Cell 2 is 101 -> 'e'
+++++++..+++.           # Cell 3, 4 and 5: human readable "l" (72+30)
>.                      # Cell 6 'o'
<<+.                    # Cell 5 32 (space)
<-.                     # Cell 4 87 ('W')
+++++++.                # Cell 5 114 (114-87 = 'o')
>.                      # Cell 6 'r'
+++.                    # Cell 7 'l'
------.                 # Cell 8 'd'
--------.               # Cell 9 33 ('!')
>>+.                    # Cell 12 new line

# End of code