brainfuck
++++++++++                 Initialize counter (cell #0) to 10
[                         Start loop
    >+++++++              Add 7 to cell #1 (will become 70)
    >++++++++++           Add 10 to cell #2 (will become 100)
    >+++                  Add 3 to cell #3 (will become 30; the loop repeated 10 times)
    >+++++++++            Add 9 to cell #4 (will become 90)
    <<<<<<<-              Decrement counter (cell #0) by 1
]                         End loop when cell #0 is 0

# Prepare memory cells to hold the values needed (starting from cell #5)
>++                     Add 2 to cell #5, will be used for 'H' (72)
>+                      Add 1 to cell #6, will be used for 'e' (101)
++++                     Add 4 to cell #7, will be used for 'l' (108)
+                         Add 1 to cell #8, will be 109 but we'll decrement later
>--                     Decrement cell #9 to be 89 for 'O' (79)
<<                       Move to cell #7

+[                      Start a loop
    >+++                 Increase cell #8 to 108 (for the first 'l')
    >-                   Decrement cell #9 to 78 (for 'o')
    <<<<                 Move back to start loop point
]                        End loop

# Adjust cell #8 for the second 'l'
>                       Move to cell #8
+++++                   Add 5 to cell #8 to reach 108 for 'l'
                          
>+++++>+++>--           Adjust remaining for 'W', 'o', 'r'
,                      Leave one 0 cell for space between words
[                        loop until current cell is 0 
    -                    Decrement current cell by 1
]
++++++++               Adjust cell #10 to 72 for 'H'
----------------------- Move to cell #11=100 for dot
<<<<<-                  And go forward with 
>>>.<<.>.>>>>+++<.>>>>>+.<<<<.>+.<<==.<<-# End #43a
