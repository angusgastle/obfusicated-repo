"""
Befunge-93 Script to Display "Hello World"

Befunge-93 is a two-dimensional esoteric programming language where commands
are laid out on a playfield (grid). The instruction pointer (IP) moves through 
the grid following commands, which can alter its direction and perform various
functions.

This script demonstrates displaying "Hello World" using multiple complex 
operations, data manipulations, and direction changes.
"""

>25*"!dlroW ,olleH":v      # Start by pushing the length of the string to the stack
v,,,,,v>>>>>>>>v,,,,,,v>v # Path to initialize stack with characters of "Hello, World!"
>v1<<,v<<<<<,,,,,,v,,,,v< # Move characters in reverse order into stack
>,"@",",",,,,,"!">,^,,,,, # Print characters stored on stack

^
,"@",",",",@,@,@,,,,,"^"^@
,,<25*v,,,,,v,<,,,,,,,^< # Python-like command terminated by '@' to stop program
,"@",",",",,,,,"^,,,,,@, # Terminating script with movement and mainstream operations
                         # including mirroring at certain points

# Final @ symbol to terminate execution of the Befunge program
@