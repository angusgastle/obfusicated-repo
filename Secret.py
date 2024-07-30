// Brainfuck program to display "Hello World"
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.
>++.<<+++++++++++++.>++++.<<.+++.------.--------.>+.>. 

/*
Brainfuck is a minimalistic programming language consisting of only eight commands and is known for its obscurity. Here's a breakdown of each line:

++++++++++        : Set cell #0 to 10
[                 : Loop start
    >+++++++      : Add  7 to  cell #1
    >++++++++++   : Add 10 to  cell #2
    >+++          : Add  3 to  cell #3
    >+            : Add  1 to  cell #4
    <<<<-         : Decrement  cell #0 (loop until cell #0 is 0)
]                 : Loop end (brackets matching)
>++               : Move to cell #1 and increment 2 (add 7*10 times)
.                 : Output cell #1 (H)
>+                : Move to cell #2 and increment (add 70 times)
.                 : Output cell #2 (e)
+++++++           : Increment cell #2 by 7 (add 111 times)
.                 : Output cell #2 (l)
.                 : Output cell #2 (l)
+++               : Increment cell #2 by 3 (add 114 times)
.                 : Output cell #2 (o)
>++               : Move to cell #3 and increment (add 3 times)
.                 : Output cell #3 (space)
<<+++++++++++++   : Move to cell #1 and add 11 times (add 108 times)
.                 : Output cell #1 (W)
>++++             : Move to cell #2 and increment 4 (add 118 times)
.                 : Output cell #2 (o)
<<                : Move to cell #0
.                 : Output cell #0 (r)
+++               : Increment cell #0 by 3 (add 111 times)
.                 : Output cell #0 (l)
------            : Decrement cell #0 by 6 (add 105 times)
.                 : Output cell #0 (d)
--------          : Decrement cell #0 by 8 (add 97 times)
.                 : Output cell #0 (newline)
>+                : Move to cell #3
.                 : Output cell #3 (Hello)
>                 : Move to cell #4
.                 : Output cell #4 (World)

Total: 105 bytes of code from 8 different commands.
*/