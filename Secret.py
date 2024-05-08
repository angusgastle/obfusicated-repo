brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>>>+.>++.


This is a Brainfuck program to output "Hello World". Brainfuck is an esoteric programming language consisting of only eight simple commands and an instruction pointer. Despite its minimalistic command set, Brainfuck is Turing complete.

Here's the breakdown:
- `++++++++++` sets the initial cell to 10 (this value is used to create loops).
- `[>` begins a loop.
  - `+++++++` increments the second cell to 70 (ASCII for "F").
  - `>++++++++++` increments the third cell to 100 (used later for further calculations).
  - `>+++` increments the fourth cell to 30.
  - `>+` increments the fifth cell to 10.
  - `<<<<-` decrements the first cell by 1 and moves the pointer back to the start of the loop.
- `>` move to the second cell which now has the value 70.
- `++.` increments by 2 (ASCII 72; 'H') and prints it.
- `>+.+++++++..+++.` move to the next cell, add 1 (ASCII 101; 'e'), print it, add 7 (ASCII 108; 'l'), print it twice, add 3 (ASCII 111; 'o'), and print.
- `>++.` move to the next cell, add 2 (ASCII 32; ' '), and print.
- `<<+++++++++++++++.` move back two cells, add 15 (ASCII 87; 'W'), and print.
- `>.` move one cell to the right (already at 111; 'o'), and print.
- `+++.------.--------.` add 3, subtract 6, subtract 8 (manipulating to reach various ASCII values to print 'rl', 'd').
- `>>>+.>++.` move three cells to the right, add 1 (ASCII 33; '!'), print, move one cell to the right, add 2, print (ASCII 10; newline).

This code generates the output:

Hello World!
