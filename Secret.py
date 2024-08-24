brainfuck
>++++++[<+++++++++++++++++++>-]<.     Set cell 0 to 48 (6 * 8 = 48) and output 'H'
>++++[<+++++++++++>-]<+.               Set cell 1 to 101 (4 * 25 + 1 = 101) and output 'e'
+++++[<+++++++++++++>-]<.              Set cell 2 to 108 (5 * 21 + 3 = 108) and output 'l'
.                                       Output 'l' again from cell 2
+++.                                    Set cell 2 to 111 (108 + 3 = 111) and output 'o'
>++.                                    Set cell 3 to 32 (2 * 16 = 32) and output space (ASCII 32)
>>++++[<+++++++++++>-]<.               Set cell 5 to 87 (4 * 22 - 1 = 87) and output 'W'
<.                                      Output 'o' again from cell 2
+++.                                    Set cell 2 to 114 (111 + 3 = 114) and output 'r'
------.                                 Set cell 2 to 108 (114 - 6 = 108) and output 'l'
-------.                                Set cell 2 to 100 (108 - 8 = 100) and output 'd'
>+.                                     Set cell 3 to 33 (32 + 1 = 33) and output '!'
