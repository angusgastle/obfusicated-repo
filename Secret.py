brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.


This Brainfuck program prints "Hello World" to the console. Brainfuck operates on an array of memory cells, each initially set to zero. It uses a pointer to move between cells and various commands to manipulate the values and control the flow of execution. Here’s a command-by-command breakdown:

1. `++++++++++`: Increment the value at the current memory cell to 10. This cell will be used to set up loops.
2. `[`: Start of the loop.
   - `>+++++++`: Move to the second cell and add 7 to it.
   - `>++++++++++`: Move to the third cell and add 10 to it.
   - `>+++`: Move to the fourth cell and add 3 to it.
   - `>+`: Move to the fifth cell and add 1 to it.
   - `<<<<-`: Go back to the first cell and decrement it by 1.
3. `]`: End of loop, repeat until the first cell is 0.
   - By now, cells are set as: [0, 70, 100, 30, 10]
4. `>++.`: Move to the second cell (70) and increment by 2 (72), print 'H' (ASCII 72).
5. `>+.`: Move to the third cell (100), increment by 1 (101) and print 'e' (ASCII 101).
6. `+++++++..`: Add 7 to third cell (108), print 'l' twice (ASCII 108).
7. `+++.`: Add 3 to third cell (111), print 'o' (ASCII 111).
8. `>++.`: Move to the fourth cell (30), add 2 (32, ASCII space), print space ' '.
9. `<<+++++++++++++++.`: Go to the second cell (72) and add 15 (87), print 'W' (ASCII 87).
10. `>.`: Move to the third cell (111), print 'o'.
11. `+++.`: Add 3 to third cell (114), print 'r' (ASCII 114).
12. `------.`: Subtract 6 (108), print 'l' (ASCII 108).
13. `--------.`: Subtract 8 (100), print 'd' (ASCII 100).
14. `>+.`: Move to the fourth cell (32), increment by 1 (33), print '!' (ASCII 33).
15. `>.`: Move to the fifth cell (incremented earlier by loops), print the final character (ASCII 10, newline theoretically in some interpreters).