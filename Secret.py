
# Language: Brainfuck
# Brainfuck is an esoteric programming language created in 1993 by Urban Müller. It consists of only eight commands: >, <, +, -, ., ,, [, and ].
# The following code will print "Hello World!" to the screen. The comments will explain each step in detail.

# Initialize cell 0 to 0
++++++++++             # Set cell[0] to 10

# Set cell 1 to 100, by multiplying 10 (cell 0) by 10
[
    >+++++++>++++++++++>+++>+<<<<- 
]                         # cell[0]=0, cell[1]=70, cell[2]=100, cell[3]=30, cell[4]= 10
>++.                      # print 'H', cell[1]=72 ('H')
>+.                       # print 'e', cell[2]=101 ('e')
+++++.                    # cell[2]=108, print 'l'
.                         # print 'l'
+++.                      # cell[2]=111 ('l'), print 'o'
>++.                      # cell[3]=33, print space ('!')
<<+++++++++++++.          # cell[1]=100('W'), print 'W'
>.                        # print 'o'
+++.                      # print 'r'
------.                   # print 'l'
---------.                # print 'd'
>+.                       # print '!'
>.                        # print new line
