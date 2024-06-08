brainfuck
+++++ +++++             initialize counter (cell #0) to 10
[                      
    > +++++ ++          add 7 to cell #1 (cell #1 = 7)
    > +++++ +++++      add 10 to cell #2 (cell #2 = 10)
    > +++ +++ +++      add 15 to cell #3 (cell #3 = 15)
    > ++++ ++++ +++    add 20 to cell #4 (cell #4 = 20)
    <<<< -             decrement counter (cell #0)
]                       loop until cell #0 is zero

>> +++.                output 'H'
> +.                   output 'e'
+++ +++.               advance to 'l' and output
>.                    output 'l'
<< +++++ +++ +++++ +++ ++ .   output 'o'
>>> +++++ +++++ +++++ +++++ +++ .  (space)
<< +.                      output 'W'
< ++.                    output 'o'
++++ +.                output 'r'
-------- .             output 'l'
<< +++ +++ .           output 'd'
>
>.                    output '!'

