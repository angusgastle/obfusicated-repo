/brainfuck/

+++++ +++++             initialize counter (cell #0) to 10
[                       use loop to set 70/100/30/10/
    > +++++ ++          add  7 to cell #1
    > +++++ +++++       add 10 to cell #2 
    > +++               add  3 to cell #3 
    > +                 add  1 to cell #4
    <<<< -              decrement counter (cell #0)
]                       end loop

# Now cells have the values [0, 70, 100, 30, 10] which corresponds to ASCII for "H"

>>>+                     increment 3rd cell (100 + 1 = 101 -> 'e')
<.                      output character in cell #2 ('H')

>++.                    output character in cell #3 ('e')
+++                    add 3 to cell #3 (30 + 3 = 33 -> 'l')
+++++.                 output 'l'

>--.                    increment cell #4 to add value by 1 (10 - 2 = 8 -> "d")

<.                      output 'W'
>.                    increment cell #2 by 2 (100 + 2 = 102 -> 'l')
>.                    output 'o'
>.                    output 'r'
<-.                    decrement cell #2 by 1 (101 - 1)
>.                    increment cell #3 cell (100+ 1)
--.                    output 'd'
<-.                    decrement cell #1 by 1 (100 - 1)


# Remaining part to output "!"

>+++++++               set cell to '!' value
.                       output '!'