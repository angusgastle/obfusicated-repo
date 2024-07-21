brainfuck
[ This Brainfuck program will print "Hello, World!" character by character ]
+++++++++++++++++++++++++++++++++++++++++++++
[ Set Cell 0 to 72 ]
>++++++++++++++++++++++++++++++++++++++++++++++++
[ Set Cell 1 to 108 ]
>++++++++++
[ Set Cell 2 to 10 to use later ]
<<
[
   >+>+<<-
]
[ Move 2 to the right ]
>>++++++++++++++++++++++++++++++++++++++++++++++++
[ Set Cell 3 to H (72) - 32 (40)]
. [ Print 'H' ]
<[-]++++++
[
    >++++++++++++++++<-
]
>++++++++[] 
. [ Print 'e' ]
>++++++++++[->+++++++<]>.
[ Set Cell 1 to l ]
++++++++++.
[ Move to cell 2 which contains 10 ]
[
   >-<[-]>>>++++[->++<]>[->>++++++++<<]>>[->++++++++++<]>>[-<+>]<<<<<<
] 
>>++++++++
[ Print 'l' again ]
. 
<+++++
[ Set Cell 2 to o ]
[
    >++++<>++++>++++++++++<<
]
>>. [ Print 'o' ]
.
++++++++++.
[ Set Cell 1 to comma (44) ]
<<+
[ Move to cell 0 and set to , ]
. [ Print ',' ]
>+++++++
[ set space (32) ]
<->++++
[
   -<-->+<>>>[-]++[-->+++++]<++<<+++++
]
.
>++++++++++[-<+++++++++++>]++++++++++.
<+++++[-<+++++++>]++++.
>
. 
<++.<<
>>>++++
[ Reset cell to newline character ]
[-<+++++++>]+++++++. 
.
>++++++++++++---.
<-.>++++++++[]
.[ Display newline ]
