brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.>

// Here's a breakdown of the Brainfuck code for "Hello World":
// Initialize the memory cells
// Cell [0] set to 10:                   ++++++++++
// Use loop to set values in subsequent cells
// Loop starting brace:                  [
// Increment Cell [1] by 7:              >+++++++
// Increment Cell [2] by 10:             >++++++++++
// Increment Cell [3] by 3:              >+++
// Increment Cell [4] by 1:              >+
// Move back to Cell [0] and decrement:  <<<<-]
// End of the loop
// Now Cell [1] = 70, Cell [2] = 100, Cell [3] = 30, Cell [4] = 10

// Print 'H'
// Move to Cell [1] and increment by 2:  >++
// Output 'H':                           .
// Print 'e'
// Decrement Cell [1] by 3:              >---
// Output 'e':                           .
// Print 'l'
// Increment Cell [1] by 7:              +++++++
// Output 'l':                           .
// Print 'l' again
// Output 'l':                           .
// Print 'o'
// Increment Cell [1] by 3:              +++
// Output 'o':                           .
// Print ' ' (space)
// Move to Cell [3] and decrement by 4:  >>----
// Output ' ':                           .
// Print 'W'
// Increment Cell [3] by 3:              +++
// Shift to next cell and increment by 6:>++++++
// Output 'W':                           .
// Print 'o'
// Decrement Cell [4] by 1:              -
// Shift to Cell [3] by moving back by 1:<
// Output 'o':                           .
// Print 'r'
// Decrement Cell [4] by 10:             ----------
// Shift to start cell and increment by 3:<+++
// Output 'r':                           .
// Print 'l'
// Decrement Cell [1] by 6:              ------
// Output 'l':                           .
// Print 'd'
// Decrement Cell [1] by 8:              --------
// Output 'd':                           .
// Print '!'
// Move to Cell [0] and increment by 1:  >+
// Output '!':                           .
