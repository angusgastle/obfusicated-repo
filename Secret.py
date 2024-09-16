
# Brainfuck program to print "Hello World!"
# Brainfuck is an esoteric programming language created by Urban Müller in 1993
# The language consists of only 8 commands, making it a minimalist Turing complete language
# This coded output requires understanding of Brainfuck's memory manipulation commands

# Initialize all cells to zero
# The "+" command increments the current cell's value
# The "[" starts a loop that continues until the current cell's value is zero
# The "]" ends the loop

# Initialize values needed to print "Hello World!"
# Brainfuck cells are initialized to zero; we need specific ASCII codes to print characters

# Set first cell to 72 (ASCII 'H')
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Move to second cell, set to 100
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Move to third cell, set to 87 (ASCII 'W')
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Move to fourth cell, set to 111 (ASCII 'o')
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Move to fifth cell, set to 114 (ASCII 'r')
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Move to sixth cell, set to 100 (ASCII 'd')
>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Move to seventh cell, set to 33 (ASCII '!')
>+++++++++++++++++++++++++++++++++++++++++

# Output 'H'
<. # Go to first cell, print value (H)

# Output 'e'
-.-.-.-. # Subtract 4 to get to 68, print D
++++ # Add 4 to get to 72, loop 

## Loop 'e' Logic (Execute 4 times)
[ # While current cell value is not 0
    - # Decrease the loop counter
    
    ## Increment second cell ('d' -> 'e')
    >+< # Move to second cell, Increment its value by 1, Move back to loop counter cell
    
    ## Increment/ Decrement
    - # Update first cell
]
. # Print 'e'

# Output 'l'
>++++++++++++++++++++++++++++++++++++++
. # Move to third cell, print value after manipulation (W -> l)

# Output another 'l'
. # Move to fourth cell, print value (o)

# Output 'o'
>++++++++++++++++++++++++++++++++ # Increment
. # Move to fifth cell, print value (r -> o)

# Output 'W'
>++++++++++++++++++++++++++++++++++++++
. ##Value has been adjusted to W

# Output space
>++++++++++++++++++++++++.
##Increment for space

# Output 'W'
>++++++++++++++++++++++++++++++++++++++
. ##value already adjusted to W

# Output 'o'
>+++++++++++++++++++++++++++++++++++++++++.
##Value already adjusted to o

# Ouput 'r'
>+++++++++++++++++++++++++++++++++++++++++++++++++
. ##Value already adjusted to r

# Output 'l'
>+++++++++++++++++++++++++++++++++++++++++++++.
##Value already adjusted to l

# Output 'd'
>+++++++++++++++++++++++++++++++++++++++++++++++
. ##Value already adjusted to d

# Output '!'
###Valued already adjusted
>+++++++++++++++++++++++++++++++++++++++++.
