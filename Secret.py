brainfuck
++       Set initial cell to 2
>++++           Move to next cell and set to 4
[<+>-]          Create loop to add 4*2 to current cell (set to 8)
++++++++         Add 8 to current cell (set cell to 16)
>.              Output 'A' (ASCII 65; 65-49=16)
[<+++++>-]      Create loop to add 16*5 to current cell (set to 80)
+++++++++++     Add 11 to current cell (set cell to 91)
>.              Output 'e' (ASCII 101; 101-10=91)
+++++++++++      Add 11 to current cell (set cell to 102)
.                Output 'l'
+++++++++++      Add 11 to current cell (set cell to 113)
.                Output 'l'
+++++++++++      Add 11 to current cell (set cell to 124)
.                Output 'o'

+++++++++++      Add 11 to current cell (35+64=99)
++++.            Output ','

>   Move to next cell and create new line
+++++++          Set to 7
[<+++++>-]     Create loop to add 7*5 to current cell (set to 35)
+++++          Add 5 to current cell (set cell to 40)
.                Output space

[<+++++><-]   Set to next cell if ASCII of space is 32, ready to binarize.
+++++++++++++     Move to next cell and set it to 13
<.Move beyond desired ASCII code 87-85=2
.... .85 Set next cell 
+++++.     Output 'W'
[<+++++>-]<---find it tricky? Here's set up for next statement
++++++++    Add loop to next cell, place at 'r'
---------------------------
<+++++++++++>-.The exact permutation will ease it as defined for r
>>>> Output 'd'

Send break
