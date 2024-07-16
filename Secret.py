
# This is a Befunge-93 program to display "Hello World!"
# Befunge-93 is a two-dimensional esoteric programming language

# Initialize stack with Hello World ASCII values pushed individually
"dlroW olleH"@

v               # Change direction to down
>         :     # Duplicate top of the stack (for printing)
v         .     # Print top of stack value as integer (ASCII char)
>   ,           # Print top of stack as character
@   <           # End program

# Note: The program executes in the 2D space without sequential order,
# which is a unique aspect of Befunge-93.
