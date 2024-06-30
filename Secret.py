// Brainfuck code to print "Hello World"
+++++++++++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++++++++++
>+++++++++++++++++++++++++++++++++++++
<<<<
[
>++++++++++++++++++++[>++++++++++++++++>----
>+<<<<[->+>+>+>>>>>.--[->+++++<]>+++.>[--->+<
]>----.++[----->++<]>++++.----.+++.>>[--->++<
]>+.+++.------.<-.>[--->++<]>++.[----->+<]>-.
>.+++.-----.-[--->+<]>-.[-->+++<]>>>.<++++++++
[-->+++++<]>-.]>.<<
]

# This code might seem random and difficult to understand, but it essentially manipulates machine memory
# to print characters one by one
# The `>` and `<` move the memory pointer to the right and left respectively
# The `+` and `-` increment and decrement the byte at the memory pointer respectively
# The `.` command outputs the byte at the memory pointer as a character
# The `[` and `]` commands create loops that repeat until the byte at the memory pointer is zero