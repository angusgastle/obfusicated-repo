brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.

This program is written in Brainfuck, an esoteric programming language.

- `++++++++++` sets the cell #0 to 10, which is used as a loop counter.
- `[` begins a loop that continues as long as the cell at the pointer (cell #0) is not 0.
- `>+++++++` increments seven times in cell #1 (70 when loop ends).
- `>++++++++++` increments ten times in cell #2 (100 when loop ends).
- `>+++` increments three times in cell #3 (30 when loop ends).
- `>+` increments once in cell #4 (10 when loop ends).
- `<<<<-` move back to cell #0 and decrement by 1. This moves back to the beginning of the loop and starts again until cell #0 reaches 0.
- `>` Move to cell #1, which now holds the ASCII value of 'H'.
- `.` Output 'H' (cell #1).
- `>+. ` Increment cell #2 once (101, ASCII for 'e') and output it.
- `+++++++. ` Increment cell #2 seven times and output 'l' (108).
- `.` Output 'l' again (the cell value hasn't changed).
- `+++. ` Increment cell #2 three times and output 'o' (111).
- `>++. ` Move to cell #3 and increment twice, then output ' ' (space, 32).
- `<<+++++++++++++++. ` Move to cell #1, increment it to 87 and output 'W'.
- `>. ` Move to cell #2 and output 'o'.
- `+++. ` Increment cell #2 three times and output 'r' (114).
- `------. ` Decrement cell #2 six times and output 'l' (108).
- `--------.` Decrement cell #2 eight times and output 'd' (100).
- `>+. ` Move to cell #3 and increment once, then output '!' (33).
- `>` Move to cell #4.

This code efficiently manipulates the few cells it uses to generate the string "Hello World!" by adjusting the ASCII values directly through increments and decrements. It's a great demonstration of programming using very low-level operations in an esoteric language.