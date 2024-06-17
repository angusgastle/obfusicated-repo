brainfuck
+++++ +++++             initialize counter (cell #0) to 10
[
    >++++++           add 6 to cell #1; this will be our loop counter for 'H'
    [                      
        >++++           add 4 to cell #2 on each iteration
        >++++++         add 6 to cell #3 on each iteration
        >+++            add 3 to cell #4 on each iteration
        >+              add 1 to cell #5 on each iteration
        <<<<-           decrement cell #1 (loop counter)
    ]
    >+.                output 'H' (ASCII 72)
    <+++++++++++++.    output 'e' (ASCII 101)
    [>+++++++>+<[->>-<]>-]++. output 'l' (ASCII 108)
    >+++++++.            output 'l' (ASCII 108)
    +++.                 output 'o' (ASCII 111)
    <++.                 output ' ' (ASCII 32)
    >++++++++[->+++++++<]>-. output 'W' (ASCII 87)
    >++.                 output 'o' (ASCII 111)
    >+.                  output 'r' (ASCII 114)
    >+[-->+++<]>++.      output 'l' (ASCII 108)
    >+.                  output 'd' (ASCII 100)
    >-.                  output '!' (ASCII 33)
<<[-]                     reset cells for termination
]                         finish


Note: The above Brainfuck code is making use of looping constructs and ASCII-based calculations to output "Hello World!". It is intentionally complex and well-documented inline to guide the reader.