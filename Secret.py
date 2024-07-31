brainfuck
[ This Brainfuck program prints "Hello World!" to the console.
Brainfuck uses 8 commands: > < + - . , [ ]
A Brainfuck program works on an array of memory cells, initially set to zero.
+/- increments/decrements the byte at the data pointer.
</> moves the data pointer left/right.
. prints the byte at the data pointer.
, accepts one byte of input (not used in this program).
[ loops until the byte at the data pointer is zero.
] ends a loop begun with [ if the byte at the data pointer is not zero.
This program manually increments values and utilizes loops for efficiency. ]

+++++ +++++             Increment cell 0 to 10
[                        Loop until cell 0 is zero
    >++++ +++++         Move to cell 1, increment to 10
    >++++ +++           Move to cell 2, increment to 7
    >+++                Move to cell 3, increment to 3
    >+++                Move to cell 4, increment to 3
    >++                 Move to cell 5, increment to 2
    >+                  Move to cell 6, increment to 1
    <<<<<<-             Move back to cell 0, decrement, continue loop
]

>++++ +++++             Move to cell 1, which now contains 70
>++++ +++++ ++++        Move to cell 2, which now contains 77
>>+++ +++++ +           Move to cell 4, which now contains 33
>++++ +                 Move to cell 5, which now contains 20
<<<.                    Move to cell 2, print 'H'
>---.                   Move to cell 3, print 'e'
+++++ ++..              Increment to print 'll'
+++.                    Increment to print 'o'
>+.                     Move to cell 5, increment to print ' '
<.                      Move to cell 4, print 'W'
+++..                   Increment to print 'oo'
---.                    Decrement to print 'r'
<<+.                    Move to cell 2, increment to print 'l'
>>+.                    Move to cell 4, increment to print 'd'
---.                    Decrement to print '!'
>+.                     Move to cell 5 to print newline (cell 5 contains 33, +3 is 36 which is '$' in ASCII)
                 
