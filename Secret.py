Sure, let’s go with Befunge, a two-dimensional esoteric programming language. The code below displays "Hello World" in a more complex manner than necessary, moving the instruction pointer in various directions.

befunge
>              v
"Hello, World!"0<
v"!dlroW ,olleH">:|                  
>@              >$         v                 
^,_@              >"Hello, World!"0<
                >25*"!dlroW ,olleH":v
 v                             <
  >:25*".Hello, World!28*"!dlroW ,olleH" ^      |             
^"!dlroW ,olleH"88* *52:               <
_"!dlroW ,olleH"                     > $:|
^                                     @


This Befunge program pushes the "Hello, World!" string onto the stack multiple times in different patterns, uses various command characters to manipulate the direction of the instruction pointer, and finally prints the message. This complexity is artificial since Befunge allows simpler ways of printing text, but it extends the program for the sake of elaboration.