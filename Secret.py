brainfuck
> ++++++++ # Initialize cell 1 with value 8
[
    >++++ # Increment cell 2 by 4, starting loop
    >++++++++ # Increment cell 3 by 8
    >++++++++ # Increment cell 4 by 8
    >++++++++ # Increment cell 5 by 8
    >+++++++++ # Increment cell 6 by 9
    >+++++++++++++    # Increment cell 7 by 13
    <<<<<<<<- # Decrement cell 1 by 1, resetting for next loop iteration
] # End of initialization loop
>+. # Output "H" (cell 2 value 72)
>+. # Output "e" (cell 3 value 101)
+++++. # Increment to "l" (cell 4 value 108)
. # Output "l"
+. # Increment to "o" (cell 5 value 111)
>-. # Decrement to ' ' (space, cell 6 value 32)
------. # Decrement to 'W' (cell 7 value 87)
<+. # Increment to 'o' (cell 5 value 111)
<-. # Decrement to 'r' (cell 4 value 114)
----. # Decrement to 'l' (cell 3 value 108)
<<+. # Increment to 'd' (cell 2 value 100)
