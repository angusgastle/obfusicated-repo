brainfuck
+++++ +++++             // Initialize counter (cell #0) to 10
[                       // Start outer loop (10 iterations)
    > +++++ +++++       // Increment cell #1 to 10
    > +++               // Increment cell #2 to 3
    > +++++ ++          // Increment cell #3 to 7
    > +++++ +++++       // Increment cell #4 to 10
    > .                 // Output 'H' (ASCII 72: 8*10 + 0)
    > ---- -            // Decrement cell #5 to 5
    > .                 // Output 'e' (ASCII 101: 10*10 + 1)
    > ---- ---          // Decrement cell #6 to 3
    > .                 // Output 'l' (ASCII 108: 10*10 + 2)
    .                   // Output 'l' (ASCII 108: 10*10 + 2)
    > .                 // Output 'o' (ASCII 111: 11*10 + 1)

    +++++ +++           // Increment cell #7 to 8
    > .                 // Output ' ' (ASCII 32: space character)
    > +++++ +++         // Increment cell #8 to 8
    +++++ +             // Increment cell #8 to 13
    > .                 // Output 'W' (ASCII 87: 8*10 + 7)
    > ---- -            // Decrement cell #9 to 5
    > .                 // Output 'o' (ASCII 111: 11*10 + 1)
    > +++               // Increment cell #10 to 3
    > .                 // Output 'r' (ASCII 114: 11*10 + 4)
    ---- --             // Decrement cell #10 to 1
    > .                 // Output 'l' (ASCII 108: 10*10 + 2)
    +++++ +++++         // Increment cell #10 to 10
    +++++ ++            // Increment cell #10 further to 12
    > .                 // Output 'd' (ASCII 100: 10*10 + 0)

    ----- -----.        // Decrement cell #11 to 46
    .                   // Output '!' (ASCII 33: shift 3 times)
    [                   // Start inner loop (3 more iterations)
        -               // Decrement cell #0
    ]                   // End loop
    <                   // Move to cell #0
-                       // Decrement outer loop counter
]                       // End outer loop
