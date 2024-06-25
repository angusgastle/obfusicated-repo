Brainfuck


// Brainfuck program to display "Hello World"

++++++++++                 //  Initialize memory cell #0 to 10
[                          //  Loop until memory cell #0 is zero
    >+++++++               //    Increment memory cell #1 to 70 (7 * 10)
    >++++++++++            //    Increment memory cell #2 to 100 (10 * 10)
    >+++                   //    Increment memory cell #3 to 30 (3 * 10)
    >+                     //    Increment memory cell #4 to 10 (1 * 10)
    >+                     //    Increment memory cell #5 to 10 (1 * 10)
    >+                     //    Increment memory cell #6 to 10 (1 * 10)
    >+                     //    Increment memory cell #7 to 10 (1 * 10)
    >+                     //    Increment memory cell #8 to 10 (1 * 10)
    >+                     //    Increment memory cell #9 to 10 (1 * 10)
    >+++                   //    Increment memory cell #10 to 30 (3 * 10)
    >++++++++              //    Increment memory cell #11 to 80 (8 * 10)
    <<<<<<<<<<<<<<         //    Move pointer back to memory cell #0
-                          //  Decrement value at memory cell #0
]                          // End of loop

// The rest of the program is for printing "Hello World!"

>++.                       // Output 'H' (ASCII 72 from memory cell #1)
>+.                        // Output 'e' (ASCII 101 from memory cell #2)
+++++.                     // Output 'l' (ASCII 108 from memory cell #3)
.                          // Output 'l' (second 'l' from memory cell #3)
+++.                       // Output 'o' (ASCII 111 from memory cell #4)
>++.                       // Output ' ' (ASCII 32 from memory cell #5)
<<<<<-----                 // Move pointer back to memory cell #0 and set it to 45
++++++.                    // Output 'W' (ASCII 87 from memory cell #0 + 42)
>-----.                    // Output 'o' (ASCII 111 from memory cell #1 + 39)
-----                      // Output 'r' (ASCII 114 from memory cell #1 + 42)
>+.                        // Output 'l' (ASCII 108 from memory cell #2 + 3)
++++.                      // Output 'd' (ASCII 100 from memory cell #3 + 1)
>+.                        // Output '!' (ASCII 33 from memory cell #4 + 1)
