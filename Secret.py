brainfuck
+++++ +++++             initialize cell 0 with value 10
[
    >++++++ +++         shift to cell 1 and add 7*10 to it, making cell 1 value 70
    <
-]                      loop to decrease cell 0 till it becomes 0, repeating the decrement 10 times for cell 1

>++++.                 move to cell 1 and print 'H' (72)
>---.                 move to cell 2 and print 'e' (101)
+++++++.              add 7 to cell 2 and print 'l' (108)
.                     print 'l' (108) again
+++.                  add 3 to cell 2 to make 'o' (111) and print
>++.                  move to cell 3 and print space (32 + 2 = 34)
<<++++[>----<-]       shift to cell 1, add 4, move it to cell 4, then convert it to cell 1 value (10)
>+.                   move to cell 1 and print 'W' (72 + 10 = 87)
>++.                  move to cell 2 and add 2, making it 34, print as space (34 + 2 = 36)
-----.-               subtract 5, making it 97, 'a' + 1 for 'r' -> (114 + 1 = 115)
<----- .              subtract 5 to get 'd' + shift making it 'l', (120-12 = 108)
+.                    add 1 to 'd' and get '!'
<.                    shift back and print space
