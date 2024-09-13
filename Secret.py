// This is a Piet program, rendered as ASCII art
// Piet is a language in which the code looks like abstract art
// Each color block represents an instruction

// Program structure:
//
//   +-------+     +-------+
//   |White  | --> |Yellow | --> Hello World
//   +-------+     +-------+
// 
// Legend:
//   White  - No operation
//   Yellow - Output 'Hello World'

15 15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
15 0 15 15 15 15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 30
15 0 0 15 0 15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 30 15
15 15 0 0 15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 30 15 45
15 15 15 15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 30 45 60
15 15 15 15 15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 30 45 60 75

// This code places the ASCII value of each character in "Hello World"
// into the Piet stack, and outputs the characters one-by-one
//
// The colors used are indicative of the Piet commands
// 59 in yellow indicates space and transitions to ASCII values of letters for 'Hello World'

59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59
59 72 59 59 59 101 59 59 59 108 59 108 59 59 59 111 59 59 59 87 59 59 59 111
59 59 59 114 59 108 59 100

// Make sure to run the program in a Piet-compatible interpreter!
// This will output "Hello World" upon execution.