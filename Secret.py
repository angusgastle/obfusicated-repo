///// Brainfuck Code to display "Hello World"

// Initialize memory cells
+++++ +++++ initialize cell 0 to 10 (ASCII 10)
[ move loop start
> +++++ +++ initialize cell 1 to 7 (ASCII 7)
> +++++ +++++ initialize cell 2 to 10 (ASCII 10)
> +++ initialize cell 3 to 3 (ASCII 3)
> + initialize cell 4 to 1 (ASCII 1)
<<<<<- decrement cell 0 (loop control) by 1
] loop until cell 0 is zero

// Sequence established now to store and print
> ++ . print 'H' (cell 1+2, ASCII 72)
> + . print 'e' (cell 2+1, ASCII 101)
>> . reset and print 'l' (cell 2+3, set cell 4 to 108)
. print 'l' again
> + . print 'o' (cell 3+1, ASCII 111)
<<<<< . reset cell pointer to start and move to cell 4
+. print ' ' (cell 0, ASCII 32)
> +++++ + . print 'W' starting from cell 3, with overflow to next cell (ASCII 87)
+++++ +++ . print 'o' (cell 3+1, ASCII 111)
. print 'r' (cell 4-1, ASCII 114)
<<< . reset and go to initial memory
. print 'l' again (cell 3+3)
> . print 'd' (cell 4+1)
+++ . print '!' (cell 3, ASCII 33)
++++.+++++ . end (cell 2, newline or chosen end symbol)