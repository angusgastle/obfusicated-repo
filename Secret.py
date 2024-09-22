brainfuck
[
    This Brainfuck program will output "Hello World!" to the console.
    We will use the ASCII values for the characters.
    Brainfuck uses a memory tape with an array of cells. We will use
    these cells to store our values and manipulate them to print the
    desired output.

    Starting with a blank slate:
      * Memory: [0, 0, 0, 0, 0, 0, 0, 0...]

    Let's initialize our memory cells to store the values we need.

    We will increment the first cell to the value 72 ('H'):
]
+++++++ [
    7 * 10 + 2 = 72
    Increment the first cell by 10 each iteration, 7 times, and increment it 2 more times.
    This gives us 70 + 2 = 72, which is the ASCII code for 'H'.
]
>++++++++++ [ initialize cell 2 with 80 ('P') ]
[ This will be decremented later for other letters ]
[ cell 1 now has 72 which we will need for 'H' ]
[ cell 2 now has 80 which we will break apart later ]

[
    We are going to use loops and arithmetic to set our cells.
    Now we move to write H to the console.
]
<.> [
    Print 'H' which is in cell 1.
    Move back to cell 2
    Modify value to get 'e'. ASCII value is 101.
]
+++++++ [
    7 * 10 + 1 = 101
    Decrement loop start
]
[ Counter setup for 'e' ]
< [ Move to the first cell where we print 'e' ]
.>
[
    Print 'e'
    Now, we prepare letter 'l'
]
++++++ [
    +6 for 'l'
]
.> [
    Print 'l'
]
.> [
    Print another 'l'
]
+++ [
    Adds to 111 for 'o'
]
.> [
   Print 'o'
]
[
    Now we need a space, ASCII 32
    Decrement from 80 in cell 2
]
- [
    repeated 48 times
]
.<. [
    Print space
    Decrease for 'W', ASCII 87
    Move left
]
++.-- [
    Tidy up code to set 'W'
]
< [
    Go back to first cell
]
. [
    Print 'W'
]
[
    Continue setting up the rest characters 'o', 'r', 'l', 'd', '!' 
]
[
    o
]
+++++++ [
    56 left = 111 - print 'o'
]
.> [
    Print and move to next cell
]
[
    r - ASCII 114
]
++ [
    lighter since 2
    reducing 112
    now at ready
]
.> [
    Print 'r'
]
[
    l - ASCII 108 later less
    ] ++++,,,[
]
. [
    that prints 'l'
]
> [
    new character set, post 32(bit)read
]
[
    d - ASCII 100 simple drive
]
< [
    Move
]
[]
.. [
    print 'd'
]
> [
    advance for exclam '!'
]
[
    complete
]
--- [
    final exclamation mark ASCII !
]
. [
    this is out!
]
