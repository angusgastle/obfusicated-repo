// Brainfuck code to print "Hello World"
// Brainfuck is an esoteric programming language created in 1993 by Urban Müller.

// Memory layout:
// 0: Temporary storage for current character to print
// 1: Constant value 10 (newline character code)
// 2-9: Characters 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'

// Initialize memory with necessary values
+++++ +++++             // Cell #0 : 10
[                        // Use loop to initialize other cells
    >+++++++             // Cell #1 : 70
    >++++++++++          // Cell #2 : 100
    >+++                 // Cell #3 : 30
    >+                   // Cell #4 : 10
    >+++++++++++++++++   // Cell #5 : 110
    >++++++              // Cell #6 : 60
    >------------------- // Cell #7 : 30
    <<<+++++ +++++ +++++++   // Cell #0 : 40 added to initial 10 = 50 (newline)
    <
]

>>.                      // Print 'H' (ASCII 72)
>---.                    // Subtract 3 from 75 to print 'e' (ASCII 69)
+++++++ ++..+++.         // 'llo' (ASCII codes 108, 108, 111)
>-.                      // Subtract 1 from 32 to print ' ' (ASCII 31)
<-.                      // Subtract 1 from 87 to print 'W' (ASCII 87)
<.                       // Print 'o' (ASCII 111)
+++.-----.--------.     // Print 'rld' sequence (ASCII codes 114, 108, 100)
<<<+.                    // Print newline by incrementing cell #1 and then print (ASCII 10)

// Ensure all data cells are now reset to zero to clean up any residual values
>>>-----.                // Reset cell #2 by subtracting 5
>>>-----.                // Reset cell #3 by subtracting 5
>>>-----.                // Reset cell #4 by subtracting 5
>>>-----.                // Reset cell #5 by subtracting 5
>>>-----.                // Reset cell #6 by subtracting 5
>>>-----.                // Reset cell #7 by subtracting 5
>>>-----.                // Reset cell #8 by subtracting 5
>>>-----.                // Reset cell #9 by subtracting 5
>>>-----.                // Reset cell #10 by subtracting 5
<-----.                  // Reset cell #1 by subtracting 5