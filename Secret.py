quad
Befunge-93

# The Hello World program in Befunge-93.
# Befunge-93 is a stack-based, reflective, esoteric programming language.
# This version overwrites itself several times to display "Hello World".

>              v
v  v           0 < The vertical loop that jumps to 0 on top
>1v>6*"!dlroW ,olleH">_ @
^           : < The horizontal loop that prints "Hello World"
 "!
 dlroW,
 olleH< < Each character stored in the Befunge grid
v_                            : Set up the movement of the instruction pointer
  

# Explanation of each part in this Befunge code
# The '>' and '<' move the instruction pointer right and left
# The 'v' and '^' move the instruction pointer down and up
# The "_" reflects the instruction pointer depending on the top of the stack value
# The "0", "1", "6", "*", and "!" are stack operations
# '0' pushes zero onto the stack, '1' pushes one, '6*' multiplies the top of the stack by 6
# The '"' toggles stringmode which pushes ASCII values of each character onto the stack until end quote
# The '@' ends the program

