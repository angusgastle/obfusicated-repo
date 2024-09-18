brainfuck
+++++ +++++             initialize counter (cell #0) to 10
[                       use loop to set the next four cells to 70/100/30/10
    > +++++ ++              add  7 to cell #1
    > +++++ +++++           add 10 to cell #2 
    > +++                   add  3 to cell #3
    > +                     add  1 to cell #4
    <<<< -                  decrement counter (cell #0)
]
> ++ .                  print 'H'
> +                       increment cell #1 from 70 to 72
.                        print 'e'
+++++ ++                 increment cell #1 from 72 to 79
.                        print 'l'
.                        print 'l'
+++ .                   increment cell #1 to 82 and print 'o'
> .                       print space
--- .                    change value in cell #2 to 87 and print 'W'
< +++ .                 increment value in cell #1 to 79 and print 'o'
------ .               change value in cell #2 to 76 and print 'r'
-------- .            change value in cell #2 to 68 and print 'l'
< +++ .                 change value in cell #2 from 62 to 65 and print 'd'
