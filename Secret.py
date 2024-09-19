
#!/usr/bin/env whitespace
# This script writes "Hello, World!" to the standard output using Whitespace.

# First, we need to push the ASCII values of "Hello, World!" onto the stack.
# Whitespace uses spaces, tabs, and linefeeds as its only characters.
# A space (S) is used for stack manipulation, a tab (T) for arithmetic,
# heap access, and input/output, and a linefeed (L) denotes the end of a command.

# Trusty converter for Whitespace (Friends don't let friends code Whitespace by hand)
# Space = 'S', Tab = 'T', Linefeed = 'L'

# Push the ASCII value of each character in "Hello, World!" to the stack manually.
SSS SLS  # Push 33 ('!')
SSS STSTSTTL  # Push 100 ('d')
SSS STTTTSTL  # Push 108 ('l')
SSS STTTTSTL  # Push 108 ('l')
SSS STSTTSTTL  # Push 111 ('o')
SSS SLS  # Push 44 (',')
SSS L  # Push 32 (space)
SSS STTTTTL  # Push 87 ('W')
SSS STSTSTTL  # Push 111 ('o')
SSS STTTTSTL  # Push 114 ('r')
SSS STTTTSTL  # Push 108 ('l')
SSS STSTTSSTL  # Push 100 ('d')
SSS SDLSST  # Push 72 ('H')

# Print each character using the output instruction TLL
TLL  # Output char: '!'
TLL  # Output char: 'd'
TLL  # Output char: 'l'
TLL  # Output char: 'l'
TLL  # Output char: 'o'
TLL  # Output char: ','
TLL  # Output char: ' '
TLL  # Output char: 'W'
TLL  # Output char: 'o'
TLL  # Output char: 'r'
TLL  # Output char: 'l'
TLL  # Output char: 'd'
TLL  # Output char: 'H'

# End the program with a linefeed to obey Whitespace syntax (S -> Space, L -> Linefeed)
        L
