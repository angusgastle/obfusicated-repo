brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<++++++++++++++.>>++++.>++++++++++.

[ This brainfuck script outputs "Hello World!"
  Explanation:
  1. Initialize memory with 10's (++++++++++)
  2. Loop to set up cells with required values
  3. [>+++++++>++++++++++>+++>+<<<<-]
     - Move pointer to the next cell and increment that cell
     - Cells become: 70, 100, 30, 10 (relative values)
  4. Perform output operations from each cell
     - Outputs 72 ('H'), 101 ('e'), 108 ('l'), 108 ('l'), 111 ('o')
  5. Increment pointer cells and output ' ' (space)
  6. Output remaining "World!" characters using similar cell manipulations.
  7. The end result is "Hello World!" printed.
]

