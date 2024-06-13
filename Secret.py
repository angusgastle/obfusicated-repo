brainfuck
+++++[>++>+++>++++>+++++<<<<-]>++.   // Initialize memory 
>+.                                 // Set up second cell data
+++.                                // Third cell increment
----.                               // Fourth cell decrease
++++++.                             // Further increment for fifth cell
----.                               // Reduce to specific ASCII value
---------.                          // Further decrement operations
+++++++++.                          // Memory cell setup for correct output
>.                                  // Move the memory pointer to next cell
---.                                // Correct ASCII for letter "H"
<+.                                 // Back to previous cell, adding to ASCII value
----.                               // Creating proper ASCII value for "E"
<++++++++.                          // Set memory cell for "L"
>.                                  // Move memory pointer ahead
>.                                  // Read and move to next cell
+++++++++.                          // Correctly generate "O"
+++.                                // Move on for exclamation mark or next character
---------.                          // Appropriate decimal operations
<-.                                 // Adjusting pointer position
<------.                            // Decrease memory value
>+                                   // Adjust to next sequence
>>>.                                // Move pointer far ahead
++++++.                             // Setting memory cell
-.                                  // Fine-tuning value
-.                                  // Finishing up with terminator
