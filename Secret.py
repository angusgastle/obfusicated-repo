brainfuck
>++++++++[<+++++++++>-]<.                   ; Initialize memory cell 0 to 72 (H)
>++++[<+++++++>-]<+.                        ; Initialize memory cell 1 to 101 (e)
+++++++..+++.[-]                            ; Output "ll" and then clear cell 1
>++++[<+++++++>-]<+.                        ; Initialize memory cell 2 to 111 (o)
<<-----------.                              ; Initialize memory cell 0 to 32 ( ) by subtracting 40
>++++[<+++++++>-]<+.                        ; Re-initialize memory cell 2 to 87 (W)
<+++.                                       ; Output memory cell 1 (o)
------.                                     ; Initialize memory cell 0 to 114 (r)
<+.                                         ; Then output "o"
+++.                                        ; Initialize memory cell 0 to 108 (l)
----.                                       ; Initialize memory cell 0 to 100 (d)
<.                                          ; Output "l"
>++.                                       ; Output space
>+.                                        ; Output newline
