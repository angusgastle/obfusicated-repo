
; Esolang: Brainfuck
; Brainfuck is an esoteric programming language created in 1993 by Urban Müller and notable for its extreme minimalism. This program prints "Hello, World!"

; [                 jump past matching ] if cell under current pointer is 0
; ]                 jump back to matching [ if cell under current pointer is nonzero
; +                 increment the byte at the data pointer
; -                 decrement the byte at the data pointer
; >                 increment the data pointer (move right)
; <                 decrement the data pointer (move left)
; .                 output the byte at the data pointer (ASCII value)
; ,                 accept one byte of input, storing its value in the byte at the data pointer

++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++.>++++.--------------

>+++++++++++.<+++.<+++.------.--------.>+.>.

