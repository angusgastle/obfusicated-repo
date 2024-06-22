Brainfuck:

brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.            Print 'H'
>+.                                                      Print 'e'
+++++++..+++.                                             Print 'l' 'l' 'o'
>.                                                        Print ' '
<<++++++++++++++.                                         Print 'W'
>.                                                        Print 'o'
+++.------.--------.                                      Print 'r' 'l' 'd'
>>+.                                                      Print '!'


J:

j
'hello' ; 'world'               NB. Create a list of words
string =: ''.join strings        NB. Concatenate into a single string with space

NB. Main code to print 'Hello World'
echo string
