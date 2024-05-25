; Joy language script for Hello World. Joy is a concatenative, stack-based language with postfix notation.
; This script demonstrates basic stack manipulation, function definition, and I/O operations.

; Define the characters for "Hello World" as individual quotations (each representing a word).
DEFINE CHAR_H  [
  "H" ; Push "H" onto the stack
] 

DEFINE CHAR_E  [
  "e" ; Push "e" onto the stack
]

DEFINE CHAR_L  [
  "l" ; Push "l" onto the stack
]

DEFINE CHAR_O  [
  "o" ; Push "o" onto the stack
]

DEFINE CHAR_SPACE  [
  " " ; Push a space onto the stack
]

DEFINE CHAR_W  [
  "W" ; Push "W" onto the stack
]

DEFINE CHAR_R  [
  "r" ; Push "r" onto the stack
]

DEFINE CHAR_D  [
  "d" ; Push "d" onto the stack
]

DEFINE NEWLINE [
  "\n" ; Push a newline character onto the stack
]

; Function to concatenate characters into a word
DEFINE CONCATENATE [
  SWAP ; Swap the top two elements on the stack
  CONCAT ; Concatenate the two elements
]

; Construct "Hello"
DEFINE HELLO [
  CHAR_H CHAR_E CONCATENATE
  CHAR_L CONCATENATE
  CHAR_L CONCATENATE
  CHAR_O CONCATENATE
]

; Construct "World"
DEFINE WORLD [
  CHAR_W CHAR_O CONCATENATE
  CHAR_R CONCATENATE
  CHAR_L CONCATENATE
  CHAR_D CONCATENATE
]

; Concatenate "Hello", space, and "World"
DEFINE HELLO_WORLD [
  HELLO CHAR_SPACE CONCATENATE
  WORLD CONCATENATE
]

; Output "Hello World"
DEFINE PRINT_HELLO_WORLD [
  HELLO_WORLD ; Push "Hello World" onto the stack
  PRINT ; Print the top element on the stack
  NEWLINE ; Push newline character onto the stack
  PRINT ; Print the newline
]

PRINT_HELLO_WORLD ; Execute the main function to print "Hello World"