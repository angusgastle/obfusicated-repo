# Befunge-93 example to display "Hello World"
# Befunge-93 is a two-dimensional esoteric programming language.

>v
v"Hello"<
> "World"!v
> ,,,,,, @
^_<

# Instructions:
# - The '>' and '<' characters are directional instructions.
# - The 'v' and '^' characters change the direction of the instruction pointer.
# - The ' " ' character toggles string mode. When in string mode, characters are pushed onto the stack.
# - The ' , ' character outputs the character at the top of the stack.
# - The ' @ ' character ends the program.