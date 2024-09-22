# Brainfuck program to print "Hello World!"
# Brainfuck uses eight commands, each a single character: 
# > < + - . , [ ]

# Initialize memory cells and set them to zero
++++++++++            # Set cell 0 to 10
[                     # Loop until cell 0 is zero
    >+++++++>++++++++++>+++>+<<<<- 
]                     # loop ends when cell 0 is zero

# Now memory cells are: 
# cell 1 = 70
# cell 2 = 100
# cell 3 = 30
# cell 4 = 10
# cell 5 = 0

# Modify cell values to produce required ASCII values
# H -> Cell 1
>+++                  # set Cell 1 to 72 (H)

# e -> Cell 2
>+                    # set Cell 2 to 101 (e)

# l -> Cell 3
+++                   # set Cell 3 to 108 (l)

# l -> Cell 3
>                     # move to cell 4

# o -> Cell 4
<<                    # move to cell 2
+++++++++++           # add 10

THE SPACE CHARACTER
>+++++               # add 5 to cell 4

W -> Next Cell()
<<+                  # move to cell 1

>+++++++             
>+++++++            
>+++++++            
>+++++++            
+++++                # set Cell value to 87 ( W)

# o -> Next Cell
>+++++++++           #set value to 111

# r -> Next Cell
>++++++              # set value to 114

# l -> Next Cell
>++++                # set value to 108

# d -> Next Cell
>+                   # set value to 100

# Exiting the loop
<<< 

# Print "Hello"
>>>>.                # H
<<.                  # e
+++.                 # l
.                    # l
-------.             #  o

# Print "World" 
>+.
>---.               
++++.
...+. 
>.                    # d

>.                   # Exclamation Mark