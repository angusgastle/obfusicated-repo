brainfuck
++++++++                Initialize cell 0 to 8
[                        Start loop since cell 0 is not 0
    >++++               Increment cell 1 to 4
    [                   Start loop since cell 1 is not 0
        >++             Increment cell 2 to 2
        >+++            Increment cell 3 to 3
        >+++            Increment cell 4 to 3
        >+              Increment cell 5 to 1
        <<<<-           Decrement cell 1, loop continues
    ]                   End loop when cell 1 is 0
    >+                  Increment cell 2 to 3
    >+                  Increment cell 3 to 4
    >-                  Decrement cell 4 to 2
    >>+                 Increment cell 6 to 1
    [<<]                Move to cell 4 and 3 to emphasis point
    <-                  Decrement cell 0, loop continues
]                        End of outer loop when cell 0 is 0
>++                     Increment cell 1 to 2
>+                      Increment cell 2 to 5
>+++++++                Increment cell 3 to 11
>++                     Increment cell 4 to 4
>+++++++++++            Increment cell 5 to 15
>                       Move to cell 6
++++++++++             Increment cell 6 to 10

<<<<<.                  Output 'H'
>++.                    Output 'e'
+++++++..               Output 'll'
+++.                    Output 'o'
>-.                     Move to next cell and modify for space
<.                      Output space
<+++++.                 Output 'W'
>++.                    Output 'o'
+++.                    Output 'r'
----.                   Modify for 'l'
------.                 Modify for 'd'
>+.                     Move and output '!'
