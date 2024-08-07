/// Befunge-93 program to display "Hello World" 
/// Befunge-93 is an esoteric programming language 
/// created in 1993, featuring a two-dimensional 
/// playfield to execute code.

// Initialize pointer starting to the right
> 

// Push ASCII values of 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '\n' onto stack
// H = 72, e = 101, l = 108, o = 111, space = 32, W = 87, r = 114, d = 100, newline = 10
"Hello, World!"32100111431108711110810810172

// Print all characters by popping from stack
^,v

// Loop until stack is empty using '@' to signal end
?!#@

/* The path the execution will take:
(1) '>' moves right
(2) '"' initiates a string mode where each character between quotes is pushed onto stack in reverse
(3) Path bends down reaching 'v' vertically drops through stack printing each popped character with ' , '
(4) '?' randomly decides direction
(5) '#' uses space skipping
- characters from stack till empty due to print marker,
(6) '@' the end indication ensures complete halt of command execution.
*/

// . . . End of script