// Brainfuck code that outputs "Hello World!"

// Declare an array large enough and a pointer
+++++ +++++             // 10 cells forward
[
    >+++++++            // Add 7 to cell #1
    >++++++++++         // Add 10 to cell #2
    >+++                // Add 3 to cell #3
    >+                  // Add 1 to cell #4
    <<<<-               // Go back to cell #0 and decrement it
]

// Now, set the cells to the correct ASCII values
>++.                    // 'H'
>+.                     // 'e'
+++++++..               // 'll'
+++.
----- -.                // 'o'
>++.                    // Space
<< +++++ +++++++++ +++. // 'W'
>>.                     // 'o'
+++ .                   // 'r'
----- -.                // 'l'
<<+.                    // 'd'
<.                      // '!'
>.                      // New Line (optional based on output view)