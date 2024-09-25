/~

@ Hello World in Befunge-98
@ Befunge is a two-dimensional esolang.
@ Each instruction is represented as a character in a grid.
@ The instruction pointer (IP) moves in a specific direction
@ through this grid and executes instructions.

~\2-:."

/~ Usage of instructions:
@ "v": Changes IP direction to down
@ "_": Pops value from stack, IP direction right if zero, else left
@ "#": Trampoline, skips the next cell in the direction of IP
@ "2-:": Complex sequence for calculation 
@ "\", "/", and "_": Control the IP direction
@ ",": Output character based on ASCII value
@ "@" Ends the program
~

v
> #   #              Test propulsion...                
>:#,_@_:-#              \p/>><
    +       @ #*\0123456               !#

~~~~~~~~~

@ Main logic to print "Hello, World!"

v >48*5*+1*5*2+1+,:#
"  !dlroW ,olleH"v
_               <
 >               ^
@ 

@ Start the IP moving right
>!
@ Initialize stack and push values
48*             @ Space
5*2+1+,:        @ H
4*9*1+,:        @ e
4*4*3+,:        @ l
4*4*3+,:        @ l
4*2*4,:         @ o
5*5,:           @ ,
2+3*1+,:        @ W
4*9*1+,:        @ o
5*2*3,:         @ r
5*5+1,:         @ l
2+3*1+,:        @ d
48*5,:v_ >      @ !
^               @

@ Finally terminates the IP
_               @
@               @