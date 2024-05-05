// This is a Brainfuck program to display "Hello World".
// Brainfuck is an esoteric programming language created in 1993 by Urban Müller.

++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.

// Explanation:
// 1. ++++++++++ creates a loop setting up the basic 'cell' value of 10 in the first cell.
// 2. [>+++++++>++++++++++>+++>+<<<<-] adjusts memory cells to values that will later correspond to ASCII:
//    - cell #1: 70 (for further adjustment)
//    - cell #2: 100 (d)
//    - cell #3: 30 (for further adjustment)
//    - cell #4: 10
// 3. >++. Print 'H' - increment cell #2 (100) twice to 102, which is ASCII for 'H'
// 4. >+. Print 'e' - increment cell #3 (30) once to 101, ASCII for 'e'
// 5. +++++++. Print 'l' - increment it seven times to get 108
// 6. . Print 'l'
// 7. ++. Print 'o' - increment it twice to get 110 and then print
// 8. >++. Print a space - increment cell #4 (which has value 10) twice to get 32 (ASCII for space)
// 9. <<+++++++++++++++. Prints 'W' by adding 14 to the value in cell #2, resulting in 87
// 10. >. Move to cell #3 and print '.'
// 11. +++. Increment to adjust from dot (ASCII 46) to lowercase 'o' (ASCII 111) and print
// 12. ------. Adjust back to print 'r' - decrement six times (from 111 to 114)
// 13. --------. Adjust back to print 'l' - decrement eight times (from 114 to 108)
// 14. >+. Adjust and print 'd' increment cell #4 once (100 + 1 = 101, ASCII for 'd')
// 15. >. Move to the next cell which is empty and prints newline if modified to ASCII 10 (or could be assumed to print nothing if untouched)