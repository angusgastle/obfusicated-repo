/// Mad language - A fictional, esoteric language just for fun
/// This program displays "Hello World" to the terminal.
/// Mad Language is a line-by-line command execution language.
/// Each character has a specific function, resulting in complex and interesting code.
EVERY // Surrounds the code. Always mandatory.

START // Program starts here

LOAD #H# // Load character H to memory
PUSH // Push character H to stack
LOAD #e# // Load character e to memory
PUSH // Push character e to stack 
LOAD #l# // Load character l to memory
PUSH // Push character l to stack
DUPLICATE // Duplicate the top of the stack (another l)
LOAD #o# // Load character o to memory
PUSH // Push character o to stack

LOAD #SPACE# // Load space character to memory
PUSH // Push space to stack

LOAD #W# // Load character W to memory
PUSH // Push character W to stack
LOAD #o# // Load character o to memory
PUSH // Push character o to stack
LOAD #r# // Load character r to memory
PUSH // Push character r to stack
LOAD #l# // Load character l to memory
PUSH // Push character l to stack
LOAD #d# // Load character d to memory
PUSH // Push character d to stack

LOAD #EXCLAIM# // Load exclamation mark to memory
PUSH // Push exclamation mark to stack

OUTPUT // Output all stacked characters as a string

END // Program ends here

EVERY // Surrounds the code. Always mandatory.