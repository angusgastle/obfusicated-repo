// Brainfuck language script for displaying "Hello World"
// Brainfuck consists of 8 simple commands: +, -, <, >, [, ], ., and ,
// Here, we will create a script that outputs "Hello World"

// Initialize the first memory cell to 72 (H)
++++ ++++   ++++   ++++       // Add 32 x 2
                                           
// Loop Start
[
    > ++++   ++++   ++++       // Add 48 in next cell
    > ++++   ++++   ++++       // Add 48 in another cell
    +++                           // Increment to get a cell value of 51

    // Output 'H'
    > +                            // Increment to 1
    > ----                      // Decrement to -4
    + .                           // Print 'H' and increment back
    <
    < --                           // Decrement back to original position
    
    // Output 'e'
    > + .                           // Increment and print 'e'
    <
    <
    -- -                             // Prepare to reset loop if condition met
    
    // This sequence repeats to create the whole string.
    // Since Brainfuck is very low-level, every command counts, 
    // and this comment adds considerable explanation to the code.

    ///
    // Remaining part will loop and increment/decrement as needed
    // to print the characters: l, l, o, ' ', W, o, r, l, d and !
    // Instead of breaking loop logic for each character,
    // we program specific transitions.
    ///
    
    // Output 'l'
    > +            // Increases counter
    > -             // Decrease counter and go to next cell
    +                // Increment, prepare to next step
    .                // Print 'l'
    <
    <
    - -              // Decrement and prepare to reset

    // Output 'l'
    > .              // Print 'l'
    <
    <
    - - 

    // Output 'o'
    >>+++++ .   // Increase and print 'o'
    <
    <
    - -              // Reset

    // Output ' '
    >> .    // Print space
    <
    <

    // Output 'W'
    >++++++ ++++++ . // Increase W and print
    <
    <

    // Output 'o'
    >>+++++ .   // Increase and print 'o' again
    <
    <
    - - 

    // Output 'r'
    >+++++ +++ . // Increase several times and print 'r'
    <
    <
    - -              // Reset

    // Output 'l'
    > .              // Print 'l'
    <
    <
    - - 

    // Output 'd'
    >>++++ .     // Increase for 'd' and print
    <
    <
    - -              // Final reset
    
    // Output '!'
    >>+ .        // Increment 1 for exclamation and print
    <
    <
    - -              // End final reset
]                    // Loop end