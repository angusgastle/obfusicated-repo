
/*
 * Brainfuck program to display "Hello, World!"
 *
 * Brainfuck is a minimalist programming language created in 1993.
 * It consists of only 8 commands: > < + - . , [ ]
 *
 * This program utilizes the 8 commands to print "Hello, World!" followed by a newline.
 */

// Initialize the memory cells and prepare for 'H' (72)
++++++++++             // Cell 0 initialized to 10
[
>+++++++ +++           // Cell 1 = 70
>+++++++++             // Cell 2 = 90
>+++++++++++           // Cell 3 = 120
<<<-                    // Decrement Cell 0 and repeat till zero
]

>++.                   // Output 'H' (72 from Cell 1)

// Prepare for 'e' (101)
> +++++++              // Cell 2 = 97 (90 + 7)
.                      // Output 'e' (101 from Cell 2)

// Prepare for 'l' (108)
++++ +++               // Cell 2 = 104 (97 + 7)
.                      // Output 'l' (108 from Cell 2)
.                      // Output 'l' (108 from Cell 2)

// Prepare for 'o' (111)
+++                    // Cell 2 = 107 (104 + 3)
.                      // Output 'o' (111 from Cell 2)

// Prepare for ',' (44)
>++++ +++++            // Cell 3 = 125 (120 + 5, overflow and wrap)
----------
.                      // Output ',' (44 from Cell 3)

// Prepare for ' ' (32)
< +                    // Cell 2 = 108 (107 + 1)
> .                    // Output ' ' (32 from Cell 2)

// Prepare for 'W' (87)
> +++++++++            // Cell 3 = 125 (120 + 5, wrap to negative and adjust)
 -.- - - - - - - - -.-.
                      // Output 'W' (87 from Cell 3)

// Prepare for 'o' (111)
< + + +                // Cell 2 = 111 (108 + 3)
.                      // Output 'o' (111 from Cell 2)

// Prepare for 'r' (114)
+++                    // Cell 2 = 114 (111 + 3)
.                      // Output 'r' (114 from Cell 2)

// Prepare for 'l' (108)
---                    // Cell 2 = 111 (114 - 3)
.                      // Output 'l' (108 from Cell 2)

// Prepare for 'd' (100)
----                   // Cell 2 = 104 (108 - 4)
.                      // Output 'd' (100 from Cell 2)

// Cleanup and ensure newline (10)
> + + +                // Cell 3 = 3
> ++++ +++ +           // Cell 4 initialized to 10
.                      // Output '\n' (10 from Cell 4)

// Program ends here
