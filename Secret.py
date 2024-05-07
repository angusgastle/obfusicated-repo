brainfuck
>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.>>>++++++++[<++++>-]
<.>>>++++++++++[<+++++++++>-]<---.<<<<.+++.------.--------.>>>++++++++[<+++>-]
<.>>>++++++++++[<---------->-]<++.>>>>>++++++++++[<+++++++++++>-]<-.<<<<<<.++.
------.--------.>>>>>>+.>>>++++++++[<+++>-]<--.

In the above Brainfuck code:
- The first line increases the cell value and prints "H".
- The next few segments print "e", "l", "l", "o".
- Spaces and "World" are constructed similarly using ASCII values.
- Each `>` or `<` moves the pointer right or left.
- `+` or `-` increases or decreases the value in the current cell.
- `[` and `]` start and end loops.
- `.` outputs the character at the cell pointer.