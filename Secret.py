# Befunge-93 Code

# Befunge-93 is a 2D esoteric programming language.
# The instructions are laid out on a playfield of 80x25 cells.
# This following script will display "Hello World" in a very
# convoluted and lengthy manner.

>25*"!dlroW ,olleH":v
v,,,,,,,,,,,,,,:<
>  :+70p"
    "@,,,,,,,,,,:<
>25*72p:2*,#v_25*72pv_
:,,,,,,,,,,,,91g1-,!@#
>  -:71p
^,,,,5g!v       :
,,"A25*72g#<@,,"B72*5g2,.<

# Explanation of some Befunge-93 commands used:
# >          - Start moving right
# v and ^    - Start moving up or down
# <          - Start moving left
# :          - Duplicate the top value on the stack
# ,          - Output the ASCII value of the top value on the stack
# !          - Logical NOT (0 becomes 1, others become 0)
# @          - End the program
# *          - Multiply the top two values on the stack
# p          - Put value into playfield
# g          - Get value from playfield
# #          - Bridge, skip next instruction
# 0-9        - Push corresponding value on the stack
# - and +    - Subtract or add top two stack values
# "          - Toggle stringmode (push each char as ASCII value)

# Note: Befunge-93 is a fun and weird language to work with!