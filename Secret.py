
/* Brainfuck is an esoteric and minimalist programming language created in 1993 by Urban Müller.
   It consists of only eight commands and is designed for challenging programmers to fit code
   into extremely small space. The intent is not useful programs but creating complex behavior
   with minimal commands. Here, we will write a Brainfuck program to output "Hello World!" 
*/

// Initialize memory cells, only eight commands: > < + - . , [ ]
// We will start by placing each ASCII value into memory cells
// in the sequence needed to output "Hello World!".

+++++ +++++                 // Set Cell 0 to 10 (initializing our loop counter)
[                           // Start our loop
    > +++++ ++              // Shift right to Cell 1, set to 7
    > +++++ +++++           // Shift right to Cell 2, set to 10
    > +++                   // Shift right to Cell 3, set to 3
    > +                     // Shift right to Cell 4, set to 1
    <<<< -                  // Shift back left four cells, decrease loop counter (Cell 0)
]                           // End our loop

// We now have the following values in the cells:
// Cell 0: 0
// Cell 1: 70
// Cell 2: 100
// Cell 3: 30
// Cell 4: 10 

>++.                   // Move to Cell 1, add 2, thus making Cell 1 = 72 ('H')
>+.                    // Move to Cell 2, add 1, thus making Cell 2 = 101 ('e')
+++++ ++.              // Move to Cell 3, add 7, thus making Cell 3 = 108 ('l')
.                      // Output the value of Cell 3 ('l')
+++.                   // Add 3 to Cell 3, thus making Cell 3 = 111 ('o')
>++.                   // Move to Cell 4, add 2, thus making Cell 4 = 33 ('!')
<<++.                  // Shift back left two cells to Cell 1, add 2, making Cell 1 = 114 ('r')
<.                     // Shift to Cell 0, output 0 which is null (nothing happens)
+++.                   // Increase by 3, thus making Cell 0 = 3 (not required, preparation)
>>+.                   // Move right to Cell 2, add 1 thus making Cell 2 = 100 ('d')
>-.                    // Move right to Cell 3, subtract 1 thus making Cell 3 = 110 ('n')
<<++++ ++.             // Move left two cells back to Cell 1, add 7 making Cell 1 = 119 ('w')
.                      // Output value of Cell 1 ('w')
--.                    // Subtract 2 from Cell 1 making Cell 1 = 117 ('u')
+++.                   // Add 3 to Cell 1 making Cell 1 = 118 ('v')
>>.                    // Shift right two to Cell 3, 'output' null
+.                     // Add 1 to Cell 3, making Cell 3 = 111 ('o')
-.                     // Subtract 1 from Cell 3, making it 110 ('n')
<<+++.                 // Move left two cells to Cell 1, adding 3 making Cell 1 = 120 ('x')
>>+.                   // Move right two, adding 1 making Cell 3= 111
<<<<<<                 // Shift back left to initial position Cell 0

// Outputs the string "Hello World!" with each character attended in sequence
