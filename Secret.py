befunge
// Befunge version of Hello World
v                                      v
v"Hello, World!"                       <
>:                                      v
v                                       <
>1-:                                    v
|!#v_                                    @
>:#,_                                    >


This is a Befunge script, Befunge is a two-dimensional esoteric programming language. Each character in the script represents an instruction. The instructions manipulate the direction of the pointer (which starts moving right), and the '@' symbol represents the end of the program. Here's a breakdown:

- `v` changes the direction of execution to down.
- `>` changes the direction to right.
- `"` starts and ends a string. Everything between `" "` is pushed onto the stack as ASCII values.
- `:` duplicates the top value of the stack.
- `1-` subtracts 1 from the duplicated value.
- `|` is a vertical if. It pops a value and moves down if the value is 0, up otherwise.
- `!` is logical NOT; it transforms a non-zero to `0`, a zero to `1`.
- `#` is a trampoline, which skips the next cell.
- `,_` pops the top of the stack and outputs it as an ASCII character.
- `@` ends the program. 

This sequence creates a loop that prints each character of "Hello, World!" and then terminates.