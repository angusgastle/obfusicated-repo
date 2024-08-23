Befunge-93:

# Note: Each command is explained for clarity in the comments
# Befunge-93 uses a 2D playfield of instructions

>                // Start moving right
v                // Move down
v                // Move down
" Hello ,        // Push 'Hello ,' onto the stack, character by character
@                // '@' marks the end of the program, but we haven't reached it yet, so it's ignored
!dlroW"  v       // Push 'World!' (reversed) onto the stack, character by character
^                // Move up
_                // Pop a value. If it's zero, move right; otherwise, move left
#                // Trampoline, skip the next instruction
_                // Pop a value. If it's zero, move right; otherwise, move left
#                // Trampoline, skip the next instruction
<                // Move left
:                // Duplicate the top stack value
1-               // Subtract 1 from the top value (setting up a loop counter)
!                // Logical NOT, to handle if zero
|                // Vertical if, move right if non-zero, down if zero
v                // Move down
" dlroW,olleH"@  // Push 'dlroW ,olleH' onto the stack (sorted this way for output purposes)
>                // Continue moving right
@                // End of the program

# Full script execution:
# The program uses stack-based operations to push characters and manipulate them to form "Hello World" by using complex and obfuscated methods of stack manipulation, conditional navigation, and movement directives.