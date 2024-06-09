brainfuck
>++++++++[<+++++++++>-]<.                   Output 'H'
>++++[<+++++++>-]<+.                        Output 'e'
+++++++..                                    Output 'l', 'l'
+++                                         Increment cell value to 'o'
[>+++++<-]>.                                Move to next cell and output ' '
<<.                                         Move back to 'W' cell and output 'W'
>--.                                        Output 'o'
>---.                                       Output 'r'
>++++++++.                                  Output 'l'
>----------.                                Output 'd'
<<.                                         Move back and output newline for cleanliness.
