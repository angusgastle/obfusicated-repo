brainfuck
+++++ +++++             initialize counter (cell #0) to 10
[
    > +++++ ++          add  7 to cell #1
    > +++++ +++++       add 10 to cell #2 
    > +++               add  3 to cell #3
    > ++++              add  4 to cell #4
    > +++++ ++          add  7 to cell #5
    > +++++ +           add  6 to cell #6
    > +++++ ++++        add  9 to cell #7
    <<<<<<< -           decrement counter (cell #0)
]
> ++ .                  print 'H'
> + .                   print 'e'
+++++ ++ .              print 'l'
.                       print 'l'
+++ .                   print 'o'
> ++ .                  print ' '
<<+++++ +++++ +++++ .   print 'W'
> .                     print 'o'
+++ .                   print 'r'
----- - .               print 'l'
----- --- .             print 'd'
> + .                   print '!'
