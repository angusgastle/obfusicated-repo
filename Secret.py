// GolfScript example to print "Hello World" in a confusingly complex way

"Hello, World!"    // Pushes "Hello, World!" to the stack
{                   // Start of a code block
    .               // Duplicates top of the stack
    ,               // Counts the length of the string on top of the stack
    (               // Decrements the length by 1
    2*              // Multiplies the result by 2
    (               // Decrements the result by 1
    2/              // Divides the result by 2
    |               // Combines the two top stack values using bitwise OR
}                   // End of code block
*                   // Executes the code block (top-of-stack times)
,,                  // Creates a range array from 0 to N-1 where N is the length of the string
{                   // Start of a code block for each item in the array
    .               // Duplicates the index
    2*              // Multiplies the index by 2
    ' '*            // Creates a string of spaces of the length 2*index
    \               // Swaps the top two elements on the stack
    +               // Concatenates them
    .               // Duplicates the result
    n               // Pushes a newline onto the stack
    +               // Concatenates the top two stack items
}                   // End of code block for the loop
%                   // Takes every second item from the array
zip                 // Transposes rows and columns of the array of strings
''*                 // Joins the arrays using an empty string as a delimiter
print               // Outputs the string on the stack to STDOUT

// The above code manipulates and builds strings in a convoluted way to eventually print "Hello, World!"