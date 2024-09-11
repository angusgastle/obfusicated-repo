/// Brainfuck program to print "Hello, World!"

// This program uses Brainfuck language 
// and meticulously sets data values 
// to output the string "Hello, World!".

++++++++++[>+++++++>++++++++++>+++>+<<<<-]   // Initialize memory cells
>++.                                    // Cell[1] = 72 = 'H', output 'H'
>+.                                     // Cell[2] = 101 = 'e', output 'e'
+++++++.                                // Cell[2] = 108, output 'l'
.                                       // continue to output 'l'
+++.                                    // output 'o'
>++.                                    // Cell[3] = 32 = ' ', output space
<<-----.                                // Move back to Cell[1], output ','
>>+.                                    // Move to Cell[3], 
<<---------.                            // output 'W'
<.                                      // Move to Cell[1], output 'o'
+++.                                    // output 'r'
------.                                 // output 'l'
--------.                               // output 'd'
>+.                                     // Move to Cell[2], output '!'
>.                                      // Move to Cell[3], output newline