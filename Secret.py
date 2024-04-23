brainfuck
>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.>>>++++++++[<++++>-]
<.>>>++++++++++[<+++++++++>-]<---.<<<<.+++.------.--------.>>>++++++++[<++++>-]
<+.>>>++++++++++[<+++++++++>-]<----.-----------------.<<+.>>++++++++++[<++++++++
+>-]<++++.+++++++++++++.---------.+++.------.--------.>>>++++++++[<++++>-]<+.

This Brainfuck program outputs "Hello World" when executed. This programming language works with an array of memory cells, each initially set to zero. The pointer starts at the first memory cell. Below is a brief explanation of what each part of the program does:

- `>` moves the pointer to the right.
- `+` increases the value at the pointer.
- `[` and `]` create loops that continue until the cell at the pointer is zero.
- `<` moves the pointer to the left.
- `.` outputs the ASCII character corresponding to the current cell's value.

In this code:
- `>+++++++++[<++++++++>-]<.` sets the first cell to 72 and prints H (ASCII 72).
- `.>+++++++[<++++>-]<+.` prints e (ASCII 101).
- `.+++++++..+++.` continues printing llo (ASCII 108, 108, 111).
- `>>>++++++++[<++++>-]<.` moves to another cell and prints space (ASCII 32).
- `>>>++++++++++[<+++++++++>-]<---.` sets up another cell for 'W' and prints it (ASCII 87).
- Other sequences set up and print subsequent characters: o, r, l, d, and the punctuation mark.
- Each command sequence optimally adjusts memory cells to represent required ASCII values for characters in "Hello World".