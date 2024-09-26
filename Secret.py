brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]        This sets up memory cells with values:
    // Cell 0: Initial zero
    // Cell 1: 70 (7*10)
    // Cell 2: 100(10*10)
    // Cell 3: 30  (3*10)
    // Cell 4: 10  (1*10)
>+.           Print 'H' (value = 72) by adding 2 to Cell 1
>+++++<[->++<]>+.   Move to Cell 2, increase to 87, print 'e'
+++++.          Print 'l' directly as Cell 2 = 100.
<.             Go to Cell 1, print 'l' (100-30)
+++.           Cell 2 = 100, Deduct and loop; print '0' directly.
>-.            Move to Cell 2, print ' ' directly (32, after decrementing)
<++.           Move to Cell 1, print 'W' directly (value = 87).
>+++++++.      Move to Cell 2, print 'o' directly (value = 111).
--------.-.    Print 'r' (8 decrement); print 'l' again (30 decrement)
<.             Print 'd' by moving and reducing all numbers
>.             Move cell and print '!' (10 added)
>. 